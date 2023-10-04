.headers on
-- For every order priority, count the number of line items ordered in 1995 and received (l receiptdate)
-- earlier than the commit date (l commitdate).

SELECT o_orderpriority as priority, count(l_orderkey) as item_cnt
FROM orders, lineitem
WHERE substr(o_orderdate, 1, 4) = '1995' AND 
        o_orderkey = l_orderkey AND 
            l_commitdate > l_receiptdate
GROUP BY o_orderpriority;