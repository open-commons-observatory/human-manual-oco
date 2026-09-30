<!-- Generated from data/ by .tad/tools/render.py. Do not edit by hand. -->

# Session Log

<a id="sibo-sifo-launch"></a>
### Запуск мануала: тема SIBO/SIFO

Entry date
: 2026-09-30

Done
: Репозиторий создан из шаблона creation-guidelines/text-as-data-template. Схема расширена под мануал: topics (иерархия через relations/subtopic-of), facts (statement + короткая цитата + перевод + статус доказательности), sources, fact_sources (цитирование). Присланный пользователем текст по СИБР/СИФО проверен по первоисточникам (ACG 2020, Merck Manual, AMBOSS, Nutrients 2025, Chedid 2014, BRIEF-SIBO protocol, обзор по функциональной диспепсии, обзор по биоплёнкам, JHR case report) и переписан с явными статусами: confirmed / preliminary / mechanistic / disputed / insufficient-evidence.

Considered
: Единая англоязычная схема с _ru/_en колонками вместо раздельных таблиц per-locale - проще поддерживать consistency и проще генерировать оба языка одним проходом рендера.

Rejected
: Не стал трогать .tad/tools/render.py (даёт только плоские per-table страницы) - вместо этого двуязычный рендер с хлебными крошками сделан отдельным скриптом bin/render_manual.py, чтобы не терять возможность git subrepo pull обновлений движка.


<a id="narrative-and-pager"></a>
### Сквозная статья и book-style пейджер

Entry date
: 2026-09-30

Done
: topics получил narrative_ru/narrative_en (длинные абзацы, отдельные от терсе summary_*). bin/render_manual.py: render_story() собирает /ru|en/story.md конкатенацией narrative_* всех topics в порядке обхода дерева (тот же порядок, что и в оглавлении), с оглавлением-якорями и ссылками 'подробнее' на страницу каждого раздела. На каждой странице раздела внизу добавлен prev/next пейджер по тому же линейному порядку (READING_ORDER).

Considered
: Хранить нарратив как отдельные абзацы по фактам (narrative на уровне facts, не topics) - отклонено: факты специально терсе и атомарны для переиспользования в карточках/цитатах; нарратив - это связующая проза МЕЖДУ фактами, ей место на уровне topic, не factов.

Rejected
: Не стал делать единый глобальный markdown-файл со статьёй вручную - тогда правка стала бы второй копией того же контента, а не тем же полем, что и в разделе; смысл TAD в этом и был.
