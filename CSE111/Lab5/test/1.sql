.headers on

-- SELECT n_name, COUNT(n_name) as cust_cnt
-- FROM customer, nation, region
-- WHERE c_nationkey = n_nationkey AND 
--         n_regionkey = r_regionkey AND 
--             r_name = 'AMERICA'
--                 GROUP BY n_name;

-- SELECT n_name, COUNT(n_name) as supp_cnt
-- FROM supplier, nation, region
-- WHERE s_nationkey = n_nationkey AND 
--         n_regionkey = r_regionkey AND 
--             r_name = 'AMERICA'
--                 GROUP BY n_name;

SELECT n_name
FROM orders, lineitem, (
    SELECT c_custkey
    FROM customer, nation, region
    WHERE c_nationkey = n_nationkey AND 
            n_regionkey = r_regionkey AND 
                r_name = 'AMERICA'
) as sq1,
(
    SELECT s_suppkey
    FROM supplier, nation, region
    WHERE s_nationkey = n_nationkey AND 
            n_regionkey = r_regionkey AND 
                r_name = 'AMERICA'
) as sq2
WHERE o_custkey = sq1.c_custkey AND 
        l_suppkey = sq2.s_suppkey
GROUP BY n_name;

--     SELECT c_custkey
--     FROM customer, nation, region
--     WHERE c_nationkey = n_nationkey AND 
--             n_regionkey = r_regionkey AND 
--                 r_name = 'AMERICA'
--                     GROUP BY n_name;