-- List the number of records for each score in the table second_table

-- Select the score and count how many times each score appears, sorted by count descending
SELECT SCORE, COUNT(*) AS number
FROM second_table
GROUP BY SCORE
ORDER BY number DESC;
