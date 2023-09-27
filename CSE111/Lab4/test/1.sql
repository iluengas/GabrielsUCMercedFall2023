.headers on

SELECT n_name, count(n_name)
FROM customer, nation, orders
WHERE o_custkey = c_custkey AND
        c_nationkey = n_nationkey AND
            n_regionkey = 3
            GROUP BY n_name;
            