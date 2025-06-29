-- List all cities of California from hbtn_0d_usa
-- Use subquery to get state_id for California, sort by cities.id
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
