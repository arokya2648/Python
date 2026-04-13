-- Create the DEPARTMENT table if it does not exist
CREATE TABLE IF NOT EXISTS DEPARTMENT (
    EMPLOYEE_ID TEXT,
    NAME TEXT,
    DEPARTMENT_ID TEXT,
    MANAGER_ID TEXT,
    SALARY REAL
);

-- Insert sample data into the DEPARTMENT table
INSERT INTO DEPARTMENT (EMPLOYEE_ID, NAME, DEPARTMENT_ID, MANAGER_ID, SALARY) VALUES
('100', 'STEVEN KING', '90', '100', 24000),
('101', 'NEENA KOCHCAR', '90', '100', 17000),
('102', 'LEX DEHAAN', '90', '102', 9000),
('103', 'BRUCE LEE', '60', '103', 4800),
('104', 'DIANA WILLS', '60', '103', 25000),
('105', 'VALLI PATOR', '50', '100', 4200),
('1973', 'LUV HAMI', '60', '102', 5000),
('106', 'DAVID AUSTIN', '90', '100', 6000);
--query to count the number of employees in each department
SELECT department_id AS 'Department code', 
COUNT(*) AS 'no of employees'
FROM DEPARTMENT
GROUP BY department_id;
--query to sum the slary of each department
SELECT department_id, SUM(salary)
FROM DEPARTMENT
GROUP BY department_id;
--query to count the number of employees and sum  the slarry in each deparrtment
SELECT department_id AS 'Department Code',
COUNT(*) AS 'no of employees',
SUM(SALARY) AS 'total salary'
FROM DEPARTMENT
GROUP BY department_id;
GROUP BY department_id
--querry to sum the salary of employees witth  a specific manager
SELECT department_id AS 'Department Code',
SUM(salary) AS ''Total Salary'
FROM DEPARTMENT
WHERE MANAGER_ID='103'
GROUP BY department_id;
--query to find departments with morre than  2 employees
SELECT department_id, COUNT(*) AS 'no of employees'
FROM DEPARTMENT
GROUP BY department_id
HAVING COUNT(*) > 2;