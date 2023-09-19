.headers on

SELECT DISTINCT(nation.n_name)
FROM nation, orders, customer
WHERE orders.o_orderdate BETWEEN '1994-12-01' AND '1994-12-31' AND
        orders.o_custkey = customer.c_custkey AND 
        customer.c_nationkey = nation.n_nationkey
        ORDER BY nation.n_name asc;
