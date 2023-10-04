.headers on
-- 1. How many customers and suppliers are in every nation from AMERICA?

SELECT n_name, COUNT(o_orderkey)
FROM orders, customer, nation, region,
(
    SELECT l_orderkey as orderKey
    FROM lineitem, supplier, nation, region
    WHERE l_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                n_regionkey = r_regionkey AND 
                    r_name = 'AMERICA'
)
WHERE o_custkey = c_custkey AND 
        c_nationkey = n_nationkey AND 
            n_regionkey = r_regionkey AND 
                r_name = 'AMERICA' AND 
                    o_orderkey = orderKey
                        GROUP BY n_name;