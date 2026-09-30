-- Every i18n row must translate a real, localizable entity: a topic, a fact, or a term (sources,
-- backlog and session_log are not localized - see data/schema.sql).
WITH ids AS (SELECT id FROM topics UNION ALL SELECT id FROM facts UNION ALL SELECT id FROM terms)
SELECT DISTINCT entity_id FROM i18n WHERE entity_id NOT IN (SELECT id FROM ids);
