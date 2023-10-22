-- create tabels data base
SELECT city, AVG(value) As avg_temp
FROM temperatures
WHEN month = "7" and month = "8"
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 2;
