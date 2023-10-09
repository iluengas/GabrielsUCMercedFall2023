.headers on

-- 1. Find the supplier-customer pair(s)
--  with the most expensive (o totalprice) order(s) completed
--  (F in o orderstatus). Print the supplier name, the customer name, and the total price.

SELECT s_name as supplier, c_name as customer, o_totalprice as price
FROM lineitem, supplier, orders, customer, 
(
    SELECT MAX(o_totalprice) as maxTotal
    FROM orders
    WHERE o_orderstatus == 'F'
)
WHERE l_suppkey = s_suppkey AND 
        l_orderkey = o_orderkey AND 
            o_custkey = c_custkey AND 
                o_totalprice = maxTotal;
