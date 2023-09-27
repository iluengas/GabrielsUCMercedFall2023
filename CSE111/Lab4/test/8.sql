.headers on

SELECT count(DISTINCT o_clerk) as clerks
FROM orders, customer, nation
WHERE o_custkey = c_custkey AND
        c_nationkey = n_nationkey AND 
            n_name = 'PERU';