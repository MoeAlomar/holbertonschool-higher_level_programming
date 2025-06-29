-- List all records from the table second_table where name is not empty or NULL

-- Select score and name, ignoring records with NULL or empty name, ordered by score descending
SELECT SCORE, NAME
FROM second_table
WHERE NAME IS NOT NULL AND NAME != ''
ORDER BY SCORE DESC;
