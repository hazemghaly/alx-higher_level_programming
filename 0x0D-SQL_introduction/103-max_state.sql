-- create tabels data base
SELECT state, Max(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
