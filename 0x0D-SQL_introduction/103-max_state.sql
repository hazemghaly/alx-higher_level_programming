-- create tabels data base
SELECT city, Max(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
