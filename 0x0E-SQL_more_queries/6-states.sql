-- create tabels data base
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    name VARCHAR(256) NOT NULL,
     id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT
     );
