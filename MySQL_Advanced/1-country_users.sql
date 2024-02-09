-- Write a SQL script that creates a table users following these requirements:
-- the table should contain the following columns: id, email, name, country
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country enum('US', 'CO', 'TN') NOT NULL
);
