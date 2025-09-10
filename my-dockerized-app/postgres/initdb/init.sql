-- Create the contents of the file: /my-dockerized-app/my-dockerized-app/postgres/initdb/init.sql --

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password) VALUES
('admin', 'admin_password'),
('user1', 'user1_password'),
('user2', 'user2_password');