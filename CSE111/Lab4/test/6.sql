.headers on

SELECT s_name as supplier, o_orderpriority as priority, count(s_name) as parts
FROM orders, 
    (
        SELECT l_orderkey, l_partkey, s_name
        FROM lineitem, supplier, nation, region
        WHERE l_suppkey = s_suppkey AND 
                s_nationkey = n_nationkey AND
                    n_name = 'INDONESIA'
                    GROUP BY l_partkey
    )
WHERE o_orderkey = l_orderkey
    GROUP BY s_name, o_orderpriority;