.headers on

-- Count the number of distinct suppliers
--  that supply parts whose type contains POLISHED and have size
-- equal to any of 10, 20, 30, or 40

SELECT COUNT(DISTINCT s_suppkey) as supp_cnt
FROM supplier, partsupp, part
WHERE s_suppkey = ps_suppkey AND 
        ps_partkey = p_partkey AND 
            p_type LIKE '%POLISHED%' AND 
                (p_size = 10 OR
                    p_size = 20 OR 
                        p_size = 30 OR 
                            p_size = 40);