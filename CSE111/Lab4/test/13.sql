.headers on

SELECT customerRegion, MIN(price), r_name as suppRegion
FROM (
        SELECT r_name as customerRegion, l_extendedprice as price
        from lineitem, orders, customer, nation, region
        WHERE l_orderkey = o_orderkey AND
                o_custkey = c_custkey AND
                    c_nationkey = n_nationkey AND
                        n_nationkey = r_regionkey
    ), lineitem, supplier, nation, region
WHERE price = l_extendedprice AND
    l_suppkey = s_suppkey AND
        s_nationkey = n_nationkey AND
            n_regionkey = r_regionkey
            GROUP BY customerRegion, suppRegion
            HAVING  customerRegion <> r_name;


