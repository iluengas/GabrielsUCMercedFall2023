.headers on
-- 5. Find the number of customers who had
-- at most three orders in November 1995 (o orderdate).

SELECT SUM(customers) as customer_cnt
FROM 
(
    SELECT o_custkey, COUNT(o_custkey) as customers
    FROM orders
    WHERE strftime('%Y-%m', o_orderdate) = '1995-11'
    GROUP BY o_custkey
        HAVING COUNT(o_custkey) <= 3
);
        