-- Create table id_not_null if it doesn't exist in the database passed as an argument
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
