-- create tabels data base
SELECT score, name
FROM second_table
WHERE name EXIST
ORDER BY score DESC;
