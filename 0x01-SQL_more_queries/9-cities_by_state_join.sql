-- Lists all cities contained in the database
-- `htbn_0d_usa`.
SELECT cities.id, cities.name, states.name
  FROM cities INNER JOIN states
    ON cities.state_id = states.name
