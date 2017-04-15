-- Creating 2 users for the db: dev and prod
CREATE USER 'airbnb_user_dev'@'localhost' IDENTIFIED BY 'development1';
-- CREATE USER 'airbnb_user_prod'@'localhost' IDENTIFIED BY 'production1';

-- Creating databases: dev and prod
CREATE DATABASE IF NOT EXISTS airbnb_dev CHARACTER SET utf8 COLLATE utf8_general_ci;
-- CREATE DATABASE airbnb_prod CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Granting PRIVILEGES to users
GRANT ALL PRIVILEGES ON airbnb_dev . * TO airbnb_user_dev@localhost;
-- GRANT ALL PRIVILEGES ON airbnb_prod . * TO airbnb_user_prod;

FLUSH PRIVILEGES;
