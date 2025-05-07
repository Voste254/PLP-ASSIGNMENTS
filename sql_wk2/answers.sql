--retreiving values from payments table
SELECT checkNumber, paymentDate, amount
FROM payments;

--getting order details in pprogress and sorting
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

--displaying sales rep employees
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

--retreiving all columns and records from offices table
SELECT * 
FROM offices;

--fetching product name and quantity in stock
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
