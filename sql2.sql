CREATE TABLE salesman(salesman_id TEXT PRIMARY KEY, name TEXT, city TEXT, comission REAL);
INSERT INTO salesman (salesman_id, name, city, comission) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002', 'Nail Knite', 'Paris', 0.13),
('5005', 'Pit Alex', 'London', 0.11),
('5006', 'Mc Lyon', 'Paris', 0.14),
('5007', 'Paul Adam', 'Rome', 0.13),
('5003', 'Lauson Hen', 'San Jose', 0.12);
SELECT * FROM salesman;

CREATE TABLE orders(ord_no TEXT PRIMARRY KEY, purch_amt REAL, ord_date TEXT, customer_id TEXT, salesman_id TEXT);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
('', '', '', ),
('', '', '', ),
('', '', '', ),
('', '', '', ),
('', '', '', ),
('', '', ', );