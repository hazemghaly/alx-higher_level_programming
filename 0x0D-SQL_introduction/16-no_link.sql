-- create tabels data base
SELECT score, name
FROM second_table
WHERE name EXISTs
ORDER BY score DESC
