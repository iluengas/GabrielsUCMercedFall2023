.headers on

SELECT COUNT(DISTINCT o_orderkey) orderCount
FROM orders, customer
WHERE o_orderpriority = '1-URGENT' AND
        o_orderdate BETWEEN '1993-01-01' AND '1997-12-31' AND
         c_custkey = o_custkey AND 
            c_nationkey = 19;
