.headers on
-- 10. Find the nation(s) having customers
--  that spend the largest amount of money(o totalprice).

SELECT MAX(o_totalprice) 
FROM orders;

SELECT n_name as country 
FROM 
(
    SELECT MAX(o_totalprice) as max 
    FROM orders
), orders, customer, nation
WHERE max = o_totalprice AND 
        o_custkey = c_custkey AND 
            c_nationkey = n_nationkey;