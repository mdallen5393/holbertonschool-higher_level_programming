-- script that lists all records of the table
-- `second_table`
SELECT score, name
FROM second_table
WHERE name NOT NULL
ORDER BY score DESC, name DESC;
