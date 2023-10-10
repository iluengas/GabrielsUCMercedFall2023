.headers on
-- 11. Find the region where customers spend the largest amount of money (l extendedprice) buying items
-- from suppliers in the same region.

-- SELECT * 
-- FROM lineitem, supplier, orders, customer, nation, region
-- WHERE l_suppkey = s_suppkey AND 
--         s_nationkey = n_nationkey AND 
--             l_orderkey = o_orderkey AND 
--                 o_custkey = c_custkey AND 
--                     c_nationkey = n_nationkey AND 

SELECT r_name as region
FROM
(
    SELECT MAX(l_extendedprice), suppKey
    FROM lineitem,
    (
        SELECT DISTINCT s_suppkey as suppKey, r_name as suppReg 
        FROM supplier, nation, region
        WHERE s_nationkey = n_nationkey AND 
                n_regionkey = r_regionkey
    ),
    (
        SELECT DISTINCT o_orderkey as orderKey, r_name as custReg
        FROM orders, customer, nation, region
        WHERE o_custkey = c_custkey AND 
                c_nationkey = n_nationkey AND 
                    n_regionkey = r_regionkey
    )
    WHERE l_suppkey = suppKey AND 
            l_orderkey = orderKey AND 
                suppReg = custReg
), supplier, nation, region
WHERE suppKey = s_suppkey AND 
        s_nationkey = n_nationkey AND 
            n_regionkey = r_regionkey;