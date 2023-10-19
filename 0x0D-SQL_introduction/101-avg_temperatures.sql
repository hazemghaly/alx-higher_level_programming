-- create tabels data base
SELECT city, AVG(value) AS avg_temp
FROM temperatures
ORDER BY city
ORDER BY avg_temp DESC;
