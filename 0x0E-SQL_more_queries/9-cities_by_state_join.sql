-- Write a script that lists all cities contained in the database hbtn_0d_usa.
-- using JOIN to join cities and states tables
SELECT cities.id, cities.name, states.name FROM cities JOIN states on cities.state_id = states.id;
