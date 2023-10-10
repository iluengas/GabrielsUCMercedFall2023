.headers on
-- 14. Compute, for every country, the value of economic exchange,
-- i.e., the difference between the number
-- of items from suppliers in that country sold to customers
-- in other countries and the number of items
-- bought by local customers from foreign suppliers in 1997 (l shipdate)

SELECT s1 as country, itemsSupplied - itemsBought as economic_exchange
FROM (
    SELECT suppNat as s1, COUNT(suppNat) as itemsSupplied
    FROM lineitem,
    (
        SELECT DISTINCT s_suppkey as suppKey, n_name as suppNat 
        FROM supplier, nation
        WHERE s_nationkey = n_nationkey
    ),
    (
        SELECT DISTINCT o_orderkey as orderKey, n_name as custNat
        FROM orders, customer, nation
        WHERE o_custkey = c_custkey AND 
                c_nationkey = n_nationkey
    )
    WHERE l_suppkey = suppKey AND 
            strftime('%Y', l_shipdate) = '1997' AND
            l_orderkey = orderKey AND 
                suppNat != custNat
                GROUP BY suppNat
),
(
    SELECT custNat as c1, COUNT(custNat) as itemsBought
    FROM lineitem,
    (
        SELECT DISTINCT s_suppkey as suppKey, n_name as suppNat
        FROM supplier, nation
        WHERE s_nationkey = n_nationkey
    ),
    (
        SELECT DISTINCT o_orderkey as orderKey, n_name as custNat
        FROM orders, customer, nation
        WHERE o_custkey = c_custkey AND 
                c_nationkey = n_nationkey
    )
    WHERE l_suppkey = suppKey AND 
            strftime('%Y', l_shipdate) = '1997' AND
            l_orderkey = orderKey AND 
                suppNat != custNat
                GROUP BY custNat
)
WHERE s1 = c1;