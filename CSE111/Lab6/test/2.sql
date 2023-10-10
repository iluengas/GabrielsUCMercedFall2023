.headers on
-- 2. Find how many distinct customers have at least one order supplied
--      exclusively by suppliers from AFRICA.



SELECT COUNT(DISTINCT c_custkey) as customer_cnt
FROM lineitem, orders, customer, supplier, nation, region
WHERE l_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                l_orderkey = o_orderkey AND 
                    o_custkey = c_custkey AND 
                        c_nationkey = n_nationkey AND 
                            n_regionkey = r_regionkey AND 
                                r_name IN ('AFRICA');

