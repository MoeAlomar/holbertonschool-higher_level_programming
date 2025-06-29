-- creats a user with all privileges
-- creating user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED
BY 'user_0d_1_pwd';

-- Granting all privilegs
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'lcoalhost' WITH GRANT OPTION;

-- Apply privilege changes immediately
FLUSH PRIVILEGES;
