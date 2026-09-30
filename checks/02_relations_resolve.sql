-- Both ends of every relation must be an existing id (topics, facts, terms, sources, backlog or
-- session_log - see 01's note on the shared namespace).
WITH ids AS (
  SELECT id FROM topics UNION ALL SELECT id FROM facts UNION ALL SELECT id FROM terms
  UNION ALL SELECT id FROM sources UNION ALL SELECT id FROM backlog UNION ALL SELECT id FROM session_log
)
SELECT 'from_id' AS end_, from_id AS missing_id FROM relations WHERE from_id NOT IN (SELECT id FROM ids)
UNION ALL
SELECT 'to_id', to_id FROM relations WHERE to_id NOT IN (SELECT id FROM ids);
