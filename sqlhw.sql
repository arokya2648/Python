CREATE TABLE salesman(salesman_id TEXT PRIMARY KEY, name TEXT, city TEXT, comission REAL);
INSERT INTO salesman (salesman_id, name, city, comission) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002', 'Nail Knite', 'Paris', 0.13),
('5005', 'Pit Alex', 'London', 0.11),
('5006', 'Mc Lyon', 'Paris', 0.14),
('5007', 'Paul Adam', 'Rome', 0.13),
('5003', 'Lauson Hen', 'San Jose', 0.12);

--Query find the average comission
SELECT AVG(comission) AS Average_Comission
FROM salesman;
--Query salesman whose name has letter a and is frrom paris
SELECT * FROM salesman WHERE name LIKE '%a%' AND city='Paris';
--Query find the salesman with maximum comission
SELECT MAX(comission) AS max_comission
FROM salesman;
--Query find the salesman with the least comission
SELECT MIN(comission) AS minimum_comission
FROM salesman;
--Query find the sum of  all the comissions
SELECT SUM(comission) AS sum_of_comissions
FROM salesman;