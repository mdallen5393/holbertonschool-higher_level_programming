-- lists all cities of California that can be found
-- in the database `hbtn_0d_usa`.
SELECT * FROM states
WHERE name = 'California'
ORDER BY id
