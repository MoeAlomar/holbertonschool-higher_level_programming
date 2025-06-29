-- list all records with score >= 10
-- using select in specific order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
