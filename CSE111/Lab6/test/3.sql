.headers on
-- 3. Find the distinct parts (p name) ordered by customers from ASIA
--  that are supplied by exactly 3 suppliers from AFRICA.

SELECT DISTINCT p_name 
FROM (
    SELECT p_partkey as pKey
    FROM part, partsupp, supplier, nation, region
    WHERE p_partkey = ps_partkey AND 
            ps_suppkey = s_suppkey AND 
                s_nationkey = n_nationkey AND 
                    n_regionkey = r_regionkey AND 
                        r_name IN ('AFRICA')
                                GROUP BY p_partkey 
                                    HAVING COUNT(p_partkey) = 3
), lineitem, part, orders, customer, nation, region
WHERE l_partkey = pKey AND 
        l_orderkey = o_orderkey AND 
            o_custkey = c_custkey AND 
                c_nationkey = n_nationkey AND 
                    n_regionkey = r_regionkey AND
                        r_name IN ('ASIA');
