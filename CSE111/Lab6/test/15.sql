.headers on
-- 15. Compute the change in the economic exchange for every country between 1996 and 1998. There should
-- be two columns in the output for every country: 1997 and 1998. Hint: use CASE to select the values
-- in the result.

SELECT s197 as country, itemsSupplied97 - itemsBought97 as _1997, itemsSupplied98 - itemsBought98 as _1998
FROM 
(
    SELECT suppNat as s197, COUNT(suppNat) as itemsSupplied97
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
    SELECT custNat as c197, COUNT(custNat) as itemsBought97
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
),
(
    SELECT suppNat as s198, COUNT(suppNat) as itemsSupplied98
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
            strftime('%Y', l_shipdate) = '1998' AND
            l_orderkey = orderKey AND 
                suppNat != custNat
                GROUP BY suppNat
), 
(
    SELECT custNat as c198, COUNT(custNat) as itemsBought98
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
            strftime('%Y', l_shipdate) = '1998' AND
            l_orderkey = orderKey AND 
                suppNat != custNat
                GROUP BY custNat
)
WHERE s197 = c197 AND 
        s197 = s198 AND 
            s198 = c198;