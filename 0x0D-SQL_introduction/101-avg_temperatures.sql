-- create tabels data base
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
ORDER BY city
ORDER BY avg_temp DESC;
