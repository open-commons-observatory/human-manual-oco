#!/usr/bin/env python3
"""render_manual.py - second render pass, on top of .tad/tools/render.py's raw per-table pages.

Repo-local (bin/, not .tad/): the generic engine only knows how to emit one flat page per table.
This script reads the same data/ (DuckDB EXPORT DATABASE folder) and additionally emits a
human-facing, bilingual, breadcrumb-navigated manual under docs/ru/ and docs/en/, built from the
topic hierarchy (relations: subtopic-of) and the facts attached to each topic (relations:
belongs-to), with citations (fact_sources -> sources). It also rewrites docs/index.md as a small
bilingual landing page. Run after `python3 .tad/tools/render.py` (see Makefile's `render` target
and `verify` recipe, which call both in sequence) - it does not touch topics.md / facts.md /
sources.md / backlog.md / session_log.md, the raw table pages the engine still owns.

Deterministic output (row order = rowid, no timestamps), same discipline as the engine, so CI can
diff docs/ for freshness exactly as it does for the engine's own pages.
"""
import os

import duckdb

DATA = "data"
DOCS = "docs"
GENERATED = "<!-- Generated from data/ by bin/render_manual.py. Do not edit by hand. -->"

LOCALES = {
    "ru": {
        "home": "Главная", "sections": "Разделы", "facts": "Факты", "status": "Статус",
        "quote": "Цитата (источник)", "quote_local": "Перевод", "sources": "Источники",
        "other_locale_label": "In English", "site_title": "Человеческий мануал",
        "status_labels": {
            "confirmed": "подтверждено", "preliminary": "предварительно, испытания идут",
            "mechanistic": "механизм известен, клинически не доказан",
            "disputed": "оспаривается / завышено в популярных источниках",
            "insufficient-evidence": "доказательств недостаточно",
        },
        "name_col": "name_ru", "summary_col": "summary_ru", "statement_col": "statement_ru",
        "quote_col": "quote_ru", "narrative_col": "narrative_ru",
        "prev": "\u2190 Предыдущая", "next": "Следующая \u2192", "story_title": "Читать как статью",
        "story_intro": "Тот же материал, что и в разделах выше, но собран в одну сквозную статью "
                       "для чтения от начала до конца. Каждый абзац здесь — то же поле "
                       "`narrative_ru` того же раздела; правка в разделе меняет и статью.",
        "toc": "Содержание",
    },
    "en": {
        "home": "Home", "sections": "Sections", "facts": "Facts", "status": "Status",
        "quote": "Quote (original)", "quote_local": "Translation", "sources": "Sources",
        "other_locale_label": "По-русски", "site_title": "The Human Manual",
        "status_labels": {
            "confirmed": "confirmed", "preliminary": "preliminary, trial ongoing",
            "mechanistic": "mechanism known, not clinically proven",
            "disputed": "disputed / overstated in popular sources",
            "insufficient-evidence": "insufficient evidence",
        },
        "name_col": "name_en", "summary_col": "summary_en", "statement_col": "statement_en",
        "quote_col": "quote", "narrative_col": "narrative_en",
        "prev": "\u2190 Previous", "next": "Next \u2192", "story_title": "Read as one article",
        "story_intro": "The same material as the sections above, assembled into one continuous "
                       "read from start to finish. Each paragraph here is the same "
                       "`narrative_en` field of the same section; editing the section changes "
                       "the article too.",
        "toc": "Contents",
    },
}

con = duckdb.connect()
con.execute(f"IMPORT DATABASE '{DATA}'")


def q(sql, *params):
    return con.execute(sql, list(params)).fetchall()


topics = {r[0]: dict(zip(
    ["id", "name_ru", "name_en", "summary_ru", "summary_en", "narrative_ru", "narrative_en",
     "order_key", "tags"], r))
    for r in q("SELECT * FROM topics ORDER BY rowid")}
facts = {r[0]: dict(zip(
    ["id", "name_ru", "name_en", "statement_ru", "statement_en", "quote", "quote_ru", "status", "tags"], r))
    for r in q("SELECT * FROM facts ORDER BY rowid")}
sources = {r[0]: dict(zip(["id", "title", "url", "author", "year"], r)) for r in q("SELECT * FROM sources")}

parent_of = {c: p for c, p, rel, _ in q("SELECT * FROM relations WHERE relation = 'subtopic-of'")}
children_of = {}
for c, p in parent_of.items():
    children_of.setdefault(p, []).append(c)
for p in children_of:
    children_of[p].sort(key=lambda tid: topics[tid]["order_key"])
roots = sorted([t for t in topics if t not in parent_of], key=lambda tid: topics[tid]["order_key"])

facts_of_topic = {}
for fid, tid, rel, _ in q("SELECT * FROM relations WHERE relation = 'belongs-to'"):
    facts_of_topic.setdefault(tid, []).append(fid)

sources_of_fact = {}
for fid, sid in q("SELECT * FROM fact_sources ORDER BY rowid"):
    sources_of_fact.setdefault(fid, []).append(sid)


def flatten_reading_order(tid):
    """Depth-first, order_key order: the same sequence render_tree() prints the nav in, reused
    as the book-style prev/next path and as the section order of the assembled story page."""
    out = [tid]
    for cid in children_of.get(tid, []):
        out += flatten_reading_order(cid)
    return out


READING_ORDER = [tid for r in roots for tid in flatten_reading_order(r)]


def breadcrumb_chain(tid):
    chain = [tid]
    while chain[-1] in parent_of:
        chain.append(parent_of[chain[-1]])
    return list(reversed(chain))


def page_url(locale, tid):
    return f"/{locale}/{tid}.html"


def front_matter(locale, title, tid):
    L = LOCALES[locale]
    lines = ["---", f'title: "{title}"', f"locale: {locale}",
              f"alt_path: {page_url('en' if locale == 'ru' else 'ru', tid)}", "breadcrumb:",
              f'  - name: "{L["home"]}"', f"    url: /{locale}/"]
    for cid in breadcrumb_chain(tid):
        lines.append(f'  - name: "{topics[cid][L["name_col"]]}"')
        lines.append(f"    url: {page_url(locale, cid)}")
    lines += ["---", ""]
    return lines


def render_topic_page(locale, tid):
    L = LOCALES[locale]
    t = topics[tid]
    lines = front_matter(locale, t[L["name_col"]], tid)
    lines += [GENERATED, "", t[L["summary_col"]], ""]

    kids = children_of.get(tid, [])
    if kids:
        lines += [f"## {L['sections']}", ""]
        for cid in kids:
            c = topics[cid]
            n_facts = len(facts_of_topic.get(cid, [])) + sum(
                len(facts_of_topic.get(g, [])) for g in children_of.get(cid, []))
            lines.append(f"- [{c[L['name_col']]}]({{{{ \"{page_url(locale, cid)}\" | relative_url }}}}) "
                         f"({n_facts})" if n_facts else
                         f"- [{c[L['name_col']]}]({{{{ \"{page_url(locale, cid)}\" | relative_url }}}})")
        lines.append("")

    fids = facts_of_topic.get(tid, [])
    if fids:
        lines += [f"## {L['facts']}", ""]
        for fid in fids:
            f = facts[fid]
            lines += [f'<a id="{fid}"></a>', f"### {f[L['name_col']]}", ""]
            lines += [f[L["statement_col"]], ""]
            lines.append(L["status"])
            lines.append(f": {L['status_labels'][f['status']]}")
            lines.append("")
            if f["quote"]:
                # English original is the anchor for provenance regardless of locale; show the
                # reader's-own-language translation alongside it when one exists.
                lines.append(L["quote"])
                lines.append(f": \u00ab{f['quote']}\u00bb")
                lines.append("")
                if f["quote_ru"] and locale == "ru":
                    lines.append(L["quote_local"])
                    lines.append(f": \u00ab{f['quote_ru']}\u00bb")
                    lines.append("")
            srcs = sources_of_fact.get(fid, [])
            if srcs:
                lines.append(L["sources"])
                links = ", ".join(f"[{sources[sid]['title']}]({sources[sid]['url']})" for sid in srcs)
                lines.append(f": {links}")
                lines.append("")

    lines.append("---")
    lines.append("")
    pos = READING_ORDER.index(tid)
    pager = []
    if pos > 0:
        p = READING_ORDER[pos - 1]
        pager.append(f'[{L["prev"]}: {topics[p][L["name_col"]]}]'
                      f'({{{{ "{page_url(locale, p)}" | relative_url }}}})')
    if pos < len(READING_ORDER) - 1:
        n = READING_ORDER[pos + 1]
        pager.append(f'[{L["next"]}: {topics[n][L["name_col"]]}]'
                      f'({{{{ "{page_url(locale, n)}" | relative_url }}}})')
    lines.append(" \u00b7 ".join(pager))
    lines.append("")
    return lines


def render_tree(locale, tid, depth=0):
    L = LOCALES[locale]
    t = topics[tid]
    lines = [("  " * depth) +
             f"- [{t[L['name_col']]}]({{{{ \"{page_url(locale, tid)}\" | relative_url }}}})"]
    for cid in children_of.get(tid, []):
        lines += render_tree(locale, cid, depth + 1)
    return lines


def render_story(locale):
    """The 'one article' reading path. Assembled, not authored separately: every paragraph below
    is exactly topics[tid][narrative_ru/en], the same field the topic's own page could show (it
    doesn't, to keep that page terse) - so editing a topic's narrative in data/topics.json changes
    both this article's matching section and, if the field is ever surfaced there too, the topic
    page. Nothing here is hand-written prose sitting outside the database."""
    L = LOCALES[locale]
    lines = ["---", f'title: "{L["story_title"]}"', f"locale: {locale}",
              f"alt_path: /{'en' if locale == 'ru' else 'ru'}/story.html", "breadcrumb:",
              f'  - name: "{L["home"]}"', f"    url: /{locale}/",
              f'  - name: "{L["story_title"]}"', f"    url: /{locale}/story.html",
              "---", "", GENERATED, "", L["story_intro"], "", f"## {L['toc']}", ""]
    for tid in READING_ORDER:
        lines.append(f"- [{topics[tid][L['name_col']]}](#{tid})")
    lines.append("")
    for tid in READING_ORDER:
        t = topics[tid]
        text = t[L["narrative_col"]]
        if not text:
            continue
        lines += [f'<a id="{tid}"></a>', f"### {t[L['name_col']]}", "", text, ""]
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
              disclaimer, "",
              f'[{L["story_title"]} \u2192]({{{{ "/{locale}/story.html" | relative_url }}}})', ""]
    for r in roots:
        lines += render_tree(locale, r)
    return lines


def write(path, lines):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as fh:
        fh.write("\n".join(lines).rstrip("\n") + "\n")


for locale in LOCALES:
    write(f"{locale}/index.md", render_locale_index(locale))
    write(f"{locale}/story.md", render_story(locale))
    for tid in topics:
        write(f"{locale}/{tid}.md", render_topic_page(locale, tid))

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
    '- [Sources]({{ "/sources.html" | relative_url }})',
    "",
])

print(f"rendered {len(topics)} topics x 2 locales, {len(facts)} facts, landing page")
