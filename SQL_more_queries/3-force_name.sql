-- Create table force_name if it doesn't exist in the database passed as an argument
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
