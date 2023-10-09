.headers on
-- 2. Find how many distinct customers have at least one order supplied
--      exclusively by suppliers from AFRICA.

SELECT DISTINCT l_orderkey--COUNT(DISTINCT c_custkey) as customer_cnt
FROM lineitem, 
(
    SELECT DISTINCT s_suppkey as suppKey
    FROM lineitem, supplier, nation, region
    WHERE l_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                n_regionkey = r_regionkey AND 
                    r_name IN ('AFRICA')
)
WHERE l_suppkey != suppKey;


