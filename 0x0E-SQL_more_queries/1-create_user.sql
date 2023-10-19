-- script that lists all privileges of the MySQL users
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON yourDatabaseName . * TO 'user_0d_1'@'localhost';
