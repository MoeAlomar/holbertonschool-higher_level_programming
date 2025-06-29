-- Creating a table with name being not null
-- using simple create table with NOT NULL Constraint
CREATE TABLE force_name IF NOT EXISTS (
id INT,
name VARCHAR(256) NOT NULL
);
