# human-manual-oco

Личный "человеческий мануал": проверяемые факты о теле, здоровье и физиологии, с прямыми
короткими цитатами из первоисточников, переводом на русский и статусом доказательности у
каждого факта (`confirmed` / `preliminary` / `mechanistic` / `disputed` / `insufficient-evidence`).
Двуязычный (RU/EN), опубликован на GitHub Pages как навигируемый мануал с хлебными крошками.

- **Читать мануал:** после включения Pages (Settings -> Pages -> Deploy from a branch -> `main` /
  `/docs`) - `https://open-commons-observatory.github.io/human-manual-oco/`.
- **Работать с данными (люди или агенты):** прочитать [`AGENTS.md`](AGENTS.md), затем `make setup`
  и `make verify`.
- **Коммиты и релизы:** [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Как это устроено
`data/` - источник истины: SQL-схема (`schema.sql`), сгенерированные `COPY`-выражения
(`load.sql`) и по одному JSON-lines файлу на таблицу. Схема (см. `data/schema.sql`):

- `topics` - разделы и подразделы мануала (`name_ru`/`name_en`, `summary_ru`/`summary_en`,
  `order_key`); иерархия задаётся строками `relations` с `relation = 'subtopic-of'`.
- `facts` - собственно факты: `statement_ru`/`statement_en` (проверенное, переформулированное
  утверждение), `quote`/`quote_ru` (короткая прямая цитата из источника и перевод, опционально),
  `status` (см. выше). Привязка факта к разделу - строка `relations` с `relation = 'belongs-to'`.
- `sources` - источники (`title`, `url`, `author`, `year`). Цитирование - таблица `fact_sources`.
- `backlog`, `session_log` - стандартные для TAD-репозиториев таблицы: что запланировано и что
  реально решалось по ходу работы (и что было отвергнуто и почему).

`checks/*.sql` проверяет инварианты (уникальность id, разрешимость связей). CI (`make verify`)
гоняет два прохода рендера:

1. `.tad/tools/render.py` - общий движок (вендорится из
   [`creation-guidelines/tad-engine`](https://github.com/creation-guidelines/tad-engine) как
   `git subrepo`, см. [`.tad/README.md`](.tad/README.md)) - плоские "сырые" страницы по одной на
   таблицу (`docs/topics.md`, `docs/facts.md`, `docs/sources.md` и т.д.), полезны для отладки
   данных напрямую.
2. `bin/render_manual.py` - репо-локальный скрипт (не часть движка, поэтому правки в нём не
   мешают будущим `git subrepo pull` обновлениям `.tad/`), который по той же иерархии `topics`
   строит человекочитаемый двуязычный мануал: `docs/ru/*.md` и `docs/en/*.md`, с хлебными
   крошками и переключателем языка в шапке каждой страницы. `docs/index.md` он же перезаписывает
   в простую страницу выбора языка.

Оформление - оригинальный минимализм этого шаблона (`docs/assets/css/style.css`): моноширинный
шрифт, структура через отступы и `dl`-списки (kramdown), без цветных плашек и жирных ярлыков -
ближе к тексту RFC, чем к типичной документационной теме.

## Добавление новой темы
`bin/seed.py` - пример того, как одной Python-сессией (параметризованные `INSERT`, без проблем с
кириллицей/апострофами в SQL-литералах) наполнить `topics`/`facts`/`sources`/`relations`/
`fact_sources` и канонически экспортировать их через `EXPORT DATABASE 'data' (FORMAT json)` -
тот же механизм, что использует `.tad/tools/dc.py canon`. Для новой темы естественно написать
второй такой скрипт (или расширить `seed.py`), затем `python3 .tad/tools/render.py && python3
bin/render_manual.py` и `make verify`.

## Статус
Лицензия не выбрана. Контент - личные заметки с проверкой источников, не медицинская
рекомендация; см. дисклеймер на титульной странице мануала.
