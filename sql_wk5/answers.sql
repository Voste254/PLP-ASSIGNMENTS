
-- Drop the index named 'IdxPhone' from the 'customers' table
DROP INDEX IdxPhone ON customers;

-- Create a user named 'bob' with the password 'S$cu3r3!' for localhost only
CREATE USER 'bob'@'localhost' IDENTIFIED BY 'S$cu3r3!';

-- Grant INSERT privilege to user 'bob' on the 'salesDB' database
GRANT INSERT ON salesDB.* TO 'bob'@'localhost';

-- Change the password for user 'bob' to 'P$55!23'
ALTER USER 'bob'@'localhost' IDENTIFIED BY 'P$55!23';
