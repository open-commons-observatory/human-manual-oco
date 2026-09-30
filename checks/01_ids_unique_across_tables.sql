-- Every table with an 'id' column shares one namespace - render.py's cross-link index is global.
SELECT id, count(*) AS n FROM (
  SELECT id FROM topics
  UNION ALL SELECT id FROM facts
  UNION ALL SELECT id FROM terms
  UNION ALL SELECT id FROM sources
  UNION ALL SELECT id FROM backlog
  UNION ALL SELECT id FROM session_log
) GROUP BY id HAVING count(*) > 1;
