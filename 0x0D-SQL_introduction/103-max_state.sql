-- create tabels data base
SELECT city, max(temperature) As max_temp
FROM temperatures
GROUP BY state;
