-- create tabels data base
SELECT city, AVG(value) AS avg_temp
FROM temperatures WHERE month = "7" and month = "8"
GROUP BY city ORDER BY avg_temp DESC
LIMIT 3;
