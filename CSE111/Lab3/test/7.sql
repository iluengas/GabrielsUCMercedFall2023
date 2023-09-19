.headers on

SELECT sum(orders.o_totalprice) as total_price
FROM orders, customer
WHERE orders.o_orderdate BETWEEN '1995-01-01' AND '1995-12-31' AND
        customer.c_custkey = orders.o_custkey
        GROUP BY customer.c_nationkey
            HAVING customer.c_nationkey = 24;

