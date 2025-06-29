-- Create table unique_id if it doesn't exist in the database passed as an argument
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
