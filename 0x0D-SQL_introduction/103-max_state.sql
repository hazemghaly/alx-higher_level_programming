-- create tabels data base
SELECT city, max(temperature) AS max_temp
FROM temperatures
GROUP BY state;
