CREATE TABLE IF NOT EXISTS PRODUCTS(PRODUCT_ID TEXT, PRODUCT_NAME TEXT, SUPPLIER_ID TEXT, CATEGORY_ID TEXT, UNIT_TEXT, PRICE_REAL);
INSERT INTO  PRODUCTS(PRODUCT_ID, PRODUCT_NAME, SUPPLIER_ID, CATEGORY_ID, UNIT_TEXT, PRICE_REAL) VALUES
('1', 'CHAIS', '1', '1', '10 BOXES * 20 BAGS', 18),
('2', 'CHANG', '1', '1', '24-12 OZ BOTTLES', 19),
('3', 'ANISEED SYRUP', '1', '2', '12-550 ML BOTTLES', 10),
('4', 'CHEF ANTON SEASONING', '2', '2', '48-6 OZ JARS', 22),
('5', 'CHEF ANTON MIX', '2', '2', '36 BOXES', 21.35);

--Query to count the number of products
SELECT COUNT (PRODUCT_ID) AS Product_count
FROM PRODUCTS;

--Querry to find the  averrage prrice of the products
SELECT AVG(PRICE_REAL) AS averageprice
FROM PRODUCTS;
--Query to find the total prrice of products
SELECT SUM(PRICE_REAL) AS totalprice
FROM PRODUCTS;
--Query find the most expensive product
SELECT MAX(PRICE_REAL) AS maxprice
FROM PRODUCTS;
--Query find the cheapest product
SELECT MIN(PRICE_REAL) AS minprice
FROM PRODUCTS;
SELECT DISTINCT(PRODUCT_NAME) AS distinctproduct
FROM PRODUCTS;