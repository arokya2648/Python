CREATE TABLE IF NOT EXISTS restaurant(NAME TEXT, NEIGHBORHOOD TEXT, CUISINE TEXT, REVIEW REAL, PRICE TEXT, HEALTH TEXT);
INSERT INTO restaurant(NAME, NEIGHBORHOOD, CUISINE, REVIEW, PRICE, HEALTH)VALUES
('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),

('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),

('Pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),

('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),

('Minca', 'Downtown', 'American', 4.6, '$$$', ''),

('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),

('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),

('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$', 'A'),

('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');

--1) DISTRRICT NEIGHBOURHOODS
SELECT DISTINCT NEIGHBORHOOD
FROM restaurant;

--2) DISTINCT CUISINE TYPES
SELECT DISTINCT CUISINE
FROM restaurant;

--3) CHINESE TAKEOUT OPTIONS
SELECT * FROM restaurant
WHERE CUISINE='Chinese';

--4) RESTAURANTS WITH REVIEW 4 ANBD ABOVE
SELECT * FROM restaurant 
WHERE review >=4.0;

--5) ITALIAN RESTAURANT WITHING $$ TO $$$
SELECT * FROM restaurant
WHERE CUISINE='Italian' AND PRICE IN ('$$', '$$$');

--6) RESTAURANTS WITH PRICE EXACTLY $$$
SELECT * FROM restaurant
WHERE PRICE='$$$';

--7) RESTAURANT NAME CONTAINS CANDY
SELECT * FROM restaurant
WHERE NAME LIKE '%CANDY%';

--8) RESTAURRANTS IN MIDTOWN DOWNTOWN ORR CHINATOWN
SELECT * FROM restaurant
WHERE neighborhood IN ('Midtown', 'Downtown', 'Chinatown');

--9) health grade pending(empty value)
SELECT * FROM restaurant
WHERE HEALTH = '' OR HEALTH IS NULL;

--10) TOP4 RRESTAURANTS BASED ON REVIEWS
SELECT * FROM restaurant
ORDER BY REVIEW DESC
LIMIT 4;