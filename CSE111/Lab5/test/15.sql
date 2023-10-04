.headers on
-- . For the line items ordered in October 1994 (o orderdate),
-- find the largest discount that is smaller than the average discount among all the orders.

SELECT MAX(l_discount) as max_small_disc
FROM lineitem, 
(
    SELECT AVG(l_discount) as avgDisc
    FROM orders, lineitem
    WHERE substr(o_orderdate, 1, 7) = '1995-10' AND
                o_orderkey = l_orderkey
)
WHERE l_discount < avgDisc;