-- List the number of records for each score in the table second_table

-- Select the score and count how many times each score appears, sorted by count descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
