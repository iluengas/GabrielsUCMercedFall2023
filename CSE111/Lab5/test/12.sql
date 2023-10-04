.headers on
-- Count the number of orders made in 1995
--  in which at least one line item was received (l receiptdate)
-- by a customer later than its commit date (l commitdate).
--  List the count of such orders for every order priority.

SELECT o_orderpriority, COUNT(DISTINCT o_orderkey)
FROM orders, lineitem
WHERE substr(o_orderdate, 1, 4) = '1995' AND
        o_orderkey = l_orderkey AND
        l_receiptdate > l_commitdate
        GROUP BY o_orderpriority;

