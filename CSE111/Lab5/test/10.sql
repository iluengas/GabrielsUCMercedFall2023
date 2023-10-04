.headers on
--  How many customers are not from EUROPE or ASIA?

SELECT count(c_custkey) as cust_cnt
FROM customer, nation, region
WHERE c_nationkey = n_nationkey AND 
        n_regionkey = r_regionkey AND 
            r_name NOT IN ('ASIA', 'EUROPE');