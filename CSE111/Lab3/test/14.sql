.headers on

SELECT region.r_name, count(region.r_name)
FROM region, nation, customer, orders
WHERE orders.o_orderstatus = 'F' AND
    orders.o_custkey = customer.c_custkey AND
        customer.c_nationkey = nation.n_nationkey AND 
        nation.n_nationkey = region.r_regionkey
        GROUP BY(region.r_name);
