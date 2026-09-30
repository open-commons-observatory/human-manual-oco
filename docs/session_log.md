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
