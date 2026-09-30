#!/usr/bin/env python3
"""render_manual.py - second render pass, on top of .tad/tools/render.py's raw per-table pages.

Repo-local (bin/, not .tad/): the generic engine only knows how to emit one flat page per table.
This script reads the same data/ (DuckDB EXPORT DATABASE folder) and additionally emits a
human-facing, multilingual, breadcrumb-navigated manual under docs/<locale>/, built from the
topic hierarchy (relations: subtopic-of) and the facts attached to each topic (relations:
belongs-to), with citations (fact_sources -> sources), a per-term glossary with auto-linked
in-text references, and reverse ("used in") links on every fact and term. Run after
`python3 .tad/tools/render.py` (see Makefile's `render` target and `verify` recipe, which call
both in sequence) - it does not touch topics.md / facts.md / sources.md / backlog.md /
session_log.md, the raw table pages the engine still owns.

Sections: a topic with no subtopic-of parent IS a section (a manual-level grouping like
SIBO/SIFO); this script treats every root topic as its own section, each with its own assembled
"read as one article" page and its own prev/next reading order, so adding a second section later
is purely a data change (add another parentless topic) - no rendering-logic change.

Locales: LOCALES below lists ONLY which locales to render and this tool's own interface strings
(labels like "Home"); it is not where the manual's content lives. All actual content (topic
names/summaries/narrative, fact names/statements/quote translations, term names/explanations) is
read from the i18n table. Adding a new content locale is a data operation (insert more i18n rows
via bin/seed.py) plus one short interface-string entry below - never a schema or structural
change to how sections/topics/facts/terms relate to each other.

Deterministic output (row order = rowid, no timestamps), same discipline as the engine, so CI can
diff docs/ for freshness exactly as it does for the engine's own pages.
"""
import os
import re

import duckdb

DATA = "data"
DOCS = "docs"
GENERATED = "<!-- Generated from data/ by bin/render_manual.py. Do not edit by hand. -->"

# Interface chrome only - not manual content. See the module docstring's "Locales" note.
LOCALES = {
    "ru": {
        "home": "Главная", "sections": "Разделы", "facts": "Факты", "status": "Статус",
        "quote": "Цитата (источник)", "quote_local": "Перевод", "sources": "Источники",
        "used_in": "Используется в", "site_title": "Человеческий мануал",
        "manual_sections": "Разделы мануала",
        "status_labels": {
            "confirmed": "подтверждено", "preliminary": "предварительно, испытания идут",
            "mechanistic": "механизм известен, клинически не доказан",
            "disputed": "оспаривается / завышено в популярных источниках",
            "insufficient-evidence": "доказательств недостаточно",
        },
        "prev": "\u2190 Предыдущая", "next": "Следующая \u2192", "story_title": "Читать как статью",
        "story_intro": "Тот же материал, что и в разделах выше, но собран в одну сквозную статью "
                       "для чтения от начала до конца. Каждый абзац здесь — то же поле "
                       "`narrative` того же раздела на этом языке; правка в разделе меняет и статью.",
        "toc": "Содержание",
        "glossary_title": "Глоссарий", "glossary_intro": "Термины, которые авто-связаны прямо в "
                       "тексте мануала при первом появлении на странице.",
    },
    "en": {
        "home": "Home", "sections": "Sections", "facts": "Facts", "status": "Status",
        "quote": "Quote (original)", "quote_local": "Translation", "sources": "Sources",
        "used_in": "Used in", "site_title": "The Human Manual",
        "manual_sections": "Manual sections",
        "status_labels": {
            "confirmed": "confirmed", "preliminary": "preliminary, trial ongoing",
            "mechanistic": "mechanism known, not clinically proven",
            "disputed": "disputed / overstated in popular sources",
            "insufficient-evidence": "insufficient evidence",
        },
        "prev": "\u2190 Previous", "next": "Next \u2192", "story_title": "Read as one article",
        "story_intro": "The same material as the sections above, assembled into one continuous "
                       "read from start to finish. Each paragraph here is the same `narrative` "
                       "field of the same section in this language; editing the section changes "
                       "the article too.",
        "toc": "Contents",
        "glossary_title": "Glossary", "glossary_intro": "Terms auto-linked directly in the "
                       "manual's text on their first appearance on a page.",
    },
}

con = duckdb.connect()
con.execute(f"IMPORT DATABASE '{DATA}'")


def q(sql, *params):
    return con.execute(sql, list(params)).fetchall()


topics = {r[0]: {"id": r[0], "order_key": r[1], "tags": r[2]} for r in q("SELECT * FROM topics ORDER BY rowid")}
facts = {r[0]: {"id": r[0], "status": r[1], "quote": r[2], "tags": r[3]} for r in q("SELECT * FROM facts ORDER BY rowid")}
terms = {r[0]: {"id": r[0]} for r in q("SELECT * FROM terms ORDER BY rowid")}
sources = {r[0]: dict(zip(["id", "title", "url", "author", "year"], r)) for r in q("SELECT * FROM sources")}

# i18n[(entity_id, field, locale)] = text
i18n = {(e, f, l): t for e, f, l, t in q("SELECT * FROM i18n")}


def tr(entity_id, field, locale, default=None):
    return i18n.get((entity_id, field, locale), default)


parent_of = {c: p for c, p, rel, _ in q("SELECT * FROM relations WHERE relation = 'subtopic-of'")}
children_of = {}
for c, p in parent_of.items():
    children_of.setdefault(p, []).append(c)
for p in children_of:
    children_of[p].sort(key=lambda tid: topics[tid]["order_key"])
sections = sorted([t for t in topics if t not in parent_of], key=lambda tid: topics[tid]["order_key"])

facts_of_topic = {}
for fid, tid, rel, _ in q("SELECT * FROM relations WHERE relation = 'belongs-to'"):
    facts_of_topic.setdefault(tid, []).append(fid)

sources_of_fact = {}
for fid, sid in q("SELECT * FROM fact_sources ORDER BY rowid"):
    sources_of_fact.setdefault(fid, []).append(sid)

# Reverse index for the generic "Used in" backlink block: every relation OTHER than the two
# structural ones (subtopic-of builds the tree itself; belongs-to is already shown via the
# breadcrumb and the topic's own Facts list) becomes a visible backlink on its target, in either
# direction, exactly like .tad/tools/render.py's own relations_for() does for the raw pages -
# this is that same idea, applied to the human-facing ones.
BACKLINK_SKIP = {"subtopic-of", "belongs-to"}
incoming = {}   # to_id -> [(from_id, relation)]
outgoing = {}   # from_id -> [(to_id, relation)]
for from_id, to_id, relation, _ in q("SELECT * FROM relations"):
    if relation in BACKLINK_SKIP:
        continue
    incoming.setdefault(to_id, []).append((from_id, relation))
    outgoing.setdefault(from_id, []).append((to_id, relation))


def section_of(tid):
    while tid in parent_of:
        tid = parent_of[tid]
    return tid


def reading_order(root):
    """Depth-first, order_key order, scoped to one section: the sequence its own nav tree,
    story page, and prev/next pager all share. A topic outside this section never appears here,
    by construction - reading order does not cross section boundaries."""
    out = [root]
    for cid in children_of.get(root, []):
        out += reading_order(cid)
    return out


READING_ORDER = {root: reading_order(root) for root in sections}


def breadcrumb_chain(tid):
    chain = [tid]
    while chain[-1] in parent_of:
        chain.append(parent_of[chain[-1]])
    return list(reversed(chain))


def topic_url(locale, tid):
    return f"/{locale}/{tid}.html"


def story_url(locale, root):
    return f"/{locale}/{root}-story.html"


def glossary_url(locale):
    return f"/{locale}/glossary.html"


def display_title(locale, tid):
    """category + ': ' + name when a category is set for this topic (e.g. "Маркеры СИБР:
    Водородный"), else bare name. category is a separate i18n field, not part of name - see the
    module docstring and data/schema.sql: a topic's own identity should not hard-code which
    family it is currently grouped under."""
    name = tr(tid, "name", locale, tid)
    cat = tr(tid, "category", locale)
    return f"{cat}: {name}" if cat else name


def link(url, text):
    return f'[{text}]({{{{ "{url}" | relative_url }}}})'


def anchor_link(fragment, text):
    """Same-page link (e.g. a story page's own table of contents). Deliberately NOT passed
    through the relative_url filter link() uses - relative_url prepends site.baseurl to
    whatever it's given, which is correct for a root-relative page path but wrong for a bare
    '#id' fragment (it would point at the site root's own anchor, not stay on this page)."""
    return f"[{text}]({fragment})"


# ---------------------------------------------------------------- glossary auto-linking
# Longest term name first, so e.g. a hypothetical "СИБР водородного типа" would be tried before
# bare "СИБР" - avoids a short term swallowing part of a longer, unrelated phrase.
def _term_patterns(locale):
    pats = []
    for tid in terms:
        name = tr(tid, "name", locale)
        if name:
            pats.append((tid, name))
    pats.sort(key=lambda p: -len(p[1]))
    return pats


TERM_PATTERNS = {locale: _term_patterns(locale) for locale in LOCALES}

term_usage = {}  # term_id -> set of (locale, referencing entity_id) that link to it


def autolink_terms(locale, text, page_id, already_on_page):
    """Wrap each term's first occurrence per page in a link to its glossary entry, and record
    the usage for that term's own 'Used in' backlink list. already_on_page is the caller's
    running set of term ids already linked on the current page (passed in, mutated in place) -
    shared across every text block on one page so a term links once per page, not once per
    paragraph."""
    if not text:
        return text
    for tid, name in TERM_PATTERNS[locale]:
        if tid in already_on_page:
            continue
        pattern = re.compile(r'(?<![\w\u0400-\u04FF])' + re.escape(name) + r'(?![\w\u0400-\u04FF])')
        m = pattern.search(text)
        if not m:
            continue
        replacement = link(f"{glossary_url(locale)}#{tid}", m.group(0))
        text = text[:m.start()] + replacement + text[m.end():]
        already_on_page.add(tid)
        term_usage.setdefault(tid, set()).add((locale, page_id))
    return text


def render_backlinks(locale, entity_id):
    """Generic 'Used in' block for any entity (fact or term) that other things point at via a
    non-structural relation, or that got auto-linked from somewhere. Mirrors the engine's own
    bidirectional relations_for() display, just applied to the human-facing pages."""
    L = LOCALES[locale]
    refs = []
    for from_id, relation in incoming.get(entity_id, []):
        if from_id in topics:
            refs.append(link(topic_url(locale, from_id), display_title(locale, from_id)))
        elif from_id in facts:
            owner = next((t for t, fs in facts_of_topic.items() if from_id in fs), None)
            if owner:
                refs.append(link(f"{topic_url(locale, owner)}#{from_id}", tr(from_id, "name", locale, from_id)))
    for locale_id, page_id in sorted(term_usage.get(entity_id, [])):
        if locale_id != locale or page_id == entity_id:
            continue
        if page_id in topics:
            refs.append(link(topic_url(locale, page_id), display_title(locale, page_id)))
        elif page_id.endswith("-story") and page_id[:-len("-story")] in sections:
            root = page_id[:-len("-story")]
            refs.append(link(story_url(locale, root),
                              f'{L["story_title"]}: {display_title(locale, root)}'))
        else:
            owner = next((t for t, fs in facts_of_topic.items() if page_id in fs), None)
            if owner:
                refs.append(link(f"{topic_url(locale, owner)}#{page_id}", tr(page_id, "name", locale, page_id)))
    if not refs:
        return []
    return [L["used_in"], ": " + ", ".join(sorted(set(refs))), ""]


def front_matter(locale, title, breadcrumb_ids, alt_path):
    L = LOCALES[locale]
    lines = ["---", f'title: "{title}"', f"locale: {locale}", f"alt_path: {alt_path}",
              "breadcrumb:", f'  - name: "{L["home"]}"', f"    url: /{locale}/"]
    for cid in breadcrumb_ids:
        lines.append(f'  - name: "{display_title(locale, cid)}"')
        lines.append(f"    url: {topic_url(locale, cid)}")
    lines += ["---", ""]
    return lines


def render_topic_page(locale, tid):
    L = LOCALES[locale]
    root = section_of(tid)
    title = display_title(locale, tid)
    alt = topic_url("en" if locale == "ru" else "ru", tid)
    lines = front_matter(locale, title, breadcrumb_chain(tid), alt)
    lines += [GENERATED, ""]
    page_terms = set()
    lines += [autolink_terms(locale, tr(tid, "summary", locale, ""), tid, page_terms), ""]
    lines += render_backlinks(locale, tid)

    kids = children_of.get(tid, [])
    if kids:
        lines += [f"## {L['sections']}", ""]
        for cid in kids:
            ctitle = display_title(locale, cid)
            n_facts = len(facts_of_topic.get(cid, [])) + sum(
                len(facts_of_topic.get(g, [])) for g in children_of.get(cid, []))
            suffix = f" ({n_facts})" if n_facts else ""
            lines.append(f"- {link(topic_url(locale, cid), ctitle)}{suffix}")
        lines.append("")

    fids = facts_of_topic.get(tid, [])
    if fids:
        lines += [f"## {L['facts']}", ""]
        for fid in fids:
            f = facts[fid]
            name = tr(fid, "name", locale, fid)
            statement = autolink_terms(locale, tr(fid, "statement", locale, ""), tid, page_terms)
            lines += [f'<a id="{fid}"></a>', f"### {name}", "", statement, ""]
            lines.append(L["status"])
            lines.append(f": {L['status_labels'][f['status']]}")
            lines.append("")
            if f["quote"]:
                lines.append(L["quote"])
                lines.append(f": \u00ab{f['quote']}\u00bb")
                lines.append("")
                translated = tr(fid, "quote_translation", locale)
                if translated:
                    lines.append(L["quote_local"])
                    lines.append(f": \u00ab{translated}\u00bb")
                    lines.append("")
            srcs = sources_of_fact.get(fid, [])
            if srcs:
                lines.append(L["sources"])
                links = ", ".join(f"[{sources[sid]['title']}]({sources[sid]['url']})" for sid in srcs)
                lines.append(f": {links}")
                lines.append("")
            lines += render_backlinks(locale, fid)

    order = READING_ORDER[root]
    pos = order.index(tid)
    pager = []
    if pos > 0:
        pager.append(link(topic_url(locale, order[pos - 1]), f'{L["prev"]}: {display_title(locale, order[pos - 1])}'))
    if pos < len(order) - 1:
        pager.append(link(topic_url(locale, order[pos + 1]), f'{L["next"]}: {display_title(locale, order[pos + 1])}'))
    if pos == len(order) - 1:
        pager.append(link(story_url(locale, root), L["story_title"]))
    lines += ["---", "", " \u00b7 ".join(pager), ""]
    return lines


def render_tree(locale, tid, depth=0):
    lines = [("  " * depth) + f"- {link(topic_url(locale, tid), display_title(locale, tid))}"]
    for cid in children_of.get(tid, []):
        lines += render_tree(locale, cid, depth + 1)
    return lines


def render_story(locale, root):
    """The 'one article' reading path for ONE section. Assembled, not authored separately: every
    paragraph is exactly that topic's narrative i18n row in this locale - editing a topic's
    narrative changes the matching section of this article too. Scoped to `root`'s own subtree
    only, so a second manual section later gets its own, separate story page automatically."""
    L = LOCALES[locale]
    title = f'{L["story_title"]}: {display_title(locale, root)}'
    lines = ["---", f'title: "{title}"', f"locale: {locale}",
              f"alt_path: {story_url('en' if locale == 'ru' else 'ru', root)}", "breadcrumb:",
              f'  - name: "{L["home"]}"', f"    url: /{locale}/",
              f'  - name: "{display_title(locale, root)}"', f"    url: {topic_url(locale, root)}",
              f'  - name: "{L["story_title"]}"', f"    url: {story_url(locale, root)}",
              "---", "", GENERATED, "", L["story_intro"], "", f"## {L['toc']}", ""]
    order = READING_ORDER[root]
    for tid in order:
        lines.append(f"- {anchor_link(f'#story-{tid}', display_title(locale, tid))}")
    lines.append("")
    page_terms = set()
    for tid in order:
        text = tr(tid, "narrative", locale)
        if not text:
            continue
        text = autolink_terms(locale, text, f"{root}-story", page_terms)
        lines += [f'<a id="story-{tid}"></a>', f"### {display_title(locale, tid)}", "", text, ""]
    return lines


def render_locale_index(locale):
    L = LOCALES[locale]
    disclaimer = ("Личные заметки с проверкой источников, не медицинская рекомендация; статус "
                  "доказательности указан у каждого факта."
                  if locale == "ru" else
                  "Personal, source-checked notes, not medical advice; an evidence status is "
                  "given for every fact.")
    lines = ["---", f'title: "{L["site_title"]}"', f"locale: {locale}",
              f"alt_path: /{'en' if locale == 'ru' else 'ru'}/", "breadcrumb:",
              f'  - name: "{L["home"]}"', f"    url: /{locale}/", "---", "", GENERATED, "",
              disclaimer, "", f"## {L['manual_sections']}", ""]
    for root in sections:
        n_facts = sum(len(facts_of_topic.get(t, [])) for t in READING_ORDER[root])
        lines.append(f"- {link(topic_url(locale, root), display_title(locale, root))} ({n_facts}) "
                     f"\u00b7 {link(story_url(locale, root), L['story_title'])}")
    lines += ["", f"[{L['glossary_title']} \u2192]({{{{ \"{glossary_url(locale)}\" | relative_url }}}})", ""]
    for root in sections:
        lines += render_tree(locale, root)
    return lines


def render_glossary(locale):
    L = LOCALES[locale]
    lines = ["---", f'title: "{L["glossary_title"]}"', f"locale: {locale}",
              f"alt_path: {glossary_url('en' if locale == 'ru' else 'ru')}", "breadcrumb:",
              f'  - name: "{L["home"]}"', f"    url: /{locale}/",
              f'  - name: "{L["glossary_title"]}"', f"    url: {glossary_url(locale)}",
              "---", "", GENERATED, "", L["glossary_intro"], ""]
    for tid in sorted(terms, key=lambda t: tr(t, "name", locale, t)):
        name = tr(tid, "name", locale, tid)
        expl = tr(tid, "explanation", locale, "")
        lines += [f'<a id="{tid}"></a>', f"### {name}", "", expl, ""]
        lines += render_backlinks(locale, tid)
    return lines


def write(path, lines):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as fh:
        fh.write("\n".join(lines).rstrip("\n") + "\n")


# Topic and story pages first, so autolink_terms() populates term_usage before the glossary
# (which shows "Used in" backlinks) is rendered.
pages = {}
for locale in LOCALES:
    for tid in topics:
        pages[f"{locale}/{tid}.md"] = render_topic_page(locale, tid)
    for root in sections:
        pages[f"{locale}/{root}-story.md"] = render_story(locale, root)

for locale in LOCALES:
    write(f"{locale}/index.md", render_locale_index(locale))
    write(f"{locale}/glossary.md", render_glossary(locale))
for path, lines in pages.items():
    write(path, lines)

write("index.md", [
    "---", "title: \"Human Manual / Человеческий мануал\"", "breadcrumb: []", "---", "",
    GENERATED, "",
    "Выберите язык. / Choose a language.", "",
    '- [Русский]({{ "/ru/" | relative_url }})',
    '- [English]({{ "/en/" | relative_url }})', "",
    "Raw data tables (generated by `.tad/tools/render.py`, one page per table, for debugging or "
    "re-querying the underlying database):",
    "",
    '- [Topics]({{ "/topics.html" | relative_url }})',
    '- [Facts]({{ "/facts.html" | relative_url }})',
    '- [Terms]({{ "/terms.html" | relative_url }})',
    '- [Sources]({{ "/sources.html" | relative_url }})',
    "",
])

print(f"rendered {len(sections)} section(s), {len(topics)} topics x {len(LOCALES)} locales, "
      f"{len(facts)} facts, {len(terms)} terms, landing page")
