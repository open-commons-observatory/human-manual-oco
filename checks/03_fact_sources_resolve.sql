-- Both columns of the citation join table must resolve: fact_id into facts, source_id into sources.
SELECT 'fact_id' AS end_, fact_id AS missing_id FROM fact_sources WHERE fact_id NOT IN (SELECT id FROM facts)
UNION ALL
SELECT 'source_id', source_id FROM fact_sources WHERE source_id NOT IN (SELECT id FROM sources);
