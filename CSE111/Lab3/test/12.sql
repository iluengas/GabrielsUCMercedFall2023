.headers on

SELECT substr(o1.o_orderdate, 1, 4) as year, 
        count(*)
FROM orders o1, nation n1, customer c1
WHERE o1.o_custkey = c1.c_custkey AND
        o1.o_orderpriority = '3-MEDIUM' AND
         c1.c_nationkey = n1.n_nationkey AND
            (n1.n_name = 'ARGENTINA' OR n1.n_name = 'BRAZIL')
            GROUP BY year;
