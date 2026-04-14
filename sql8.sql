CREATE TABLE IF NOT EXISTS salesman(

salesman_id TEXT PRIMARY KEY,

name TEXT,

city TEXT,

comission TEXT

);

INSERT INTO salesman(salesman_id,name,city,comission)

VALUES

("5001","James Hoog","New York","0.15"),

("5002","Nail Knite","Paris","0.13"),

("5005","Pit Alex","London","0.11"),

("5006","Mc Lyon","Paris","0.14"),

("5007","Paul Adam","Rome","0.13"),

("5003","Lauson Hen","San Jose","0.12");

CREATE TABLE IF NOT EXISTS customer(

customer_id TEXT,

cust_name TEXT PRIMARY KEY,

city TEXT,

grade TEXT,

salesman_id TEXT

);

INSERT INTO customer(customer_id,cust_name,city,grade,salesman_id)

VALUES

("3002","nick rimando","new york","100","5001"),

("3007","brad davis","new york","200","5001"),

("3005","graham zusi","california","200","5002"),

("3008","julian green","london","300","5002"),

("3004","fabian johnson","paris","300","5006"),

("3009","geoff cameron","berlin","100","5003"),

("3003","jozy altidor","moscow","200","5007"),

("3001","brad guzan","london","","5005");

CREATE TABLE IF NOT EXISTS orders(

ord_no TEXT PRIMARY KEY,

purch_amt TEXT,

ord_date TEXT,

customer_id TEXT,

salesman_id TEXT

);

INSERT INTO Orders(ord_no,purch_amt,ord_date,customer_id,Salesman_id)

VALUES

("70001","150.5","2012-10-05","3005","5002"),

("70009","270.65","2012-09-10","3001","5001"),

("70002","65.26","2012-10-05","3002","5003"),

("70004","110.5","2012-08-17","3009","5007"),

("70007","948.5","2012-09-10","3005","5005"),

("70005","2400.6","2012-07-27","3007","5006");

--Queries
--mATCHING CUSTOMER AND SALESMAN BY CITY
SELECT customer.cust_name, salesman_name, salesman_city
FROM customer
JOIN salesman ON customer.city=salesman.city;

--linking customer to their salesman
SELECT customer.cust_name,salesman.name
FROM customer
JOIN salesman ON customer.salesman_id=salesman.salesman_id;

--Fetching orders where customers city does not match the salesmans city
SELECT orders.ord_no, customer.cust_name, orders.customer_id, orders.salesman_id
FROM orders
JOIN customers ON orderrs.customer_id=customerr.customer_id
JOIN salesman ON orders.salesman_id= salessman.salesman_id
WHERE customer.city <> salesman.city;

--fetching all orrders with customer namess
SELECT orders.ord_no, customer.cust_name
FROM orders
JOIN customer ON orders.customer_id=customer.customer_id;
--customerrs with grades
SELECT customr.cust_name AS 'customerr', customer.grade AS 'grrade'
FROM orders
JOIN Salesman ON orders.salessman_id=salesman.salesman_id
JOIN customr ON orders.customer_id=customer.customerr_id
WHERE Customer.grade IS NOT NULL
--Custtomers with salesman where comission is betweem 0,12 and 0.14
SELECT customer.cust_name AS 'Customer',
custtomer.city AS 'City',
salesman.name AS 'Salesman',
Salesman.commission
FROM customer
Join Salesman ON customer.salesman_id=salesman.salesman_id
WHERE salesman.commission BETWEEN 0.12 AND 0.14;
--calcu;ating commissions for orderrs where customerrr grade is 200 or more
SELECT orrders.ord_no, customer.cust_name, salesmam.commision AS 'commission'
Orders.purch-amt * salesman.commission AS 'commission'
FRROM orders
JOIN salesman on orders.salesman_id=salesman.salesman_id
JOIN Customer ON orders.customer_id=customer.customer_id
