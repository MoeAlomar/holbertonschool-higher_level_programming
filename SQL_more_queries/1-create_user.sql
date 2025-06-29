-- Creates the MySQL server user user_0d_1 with all privileges

-- Create user user_0d_1@localhost with password if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on the server to user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes immediately
FLUSH PRIVILEGES;
