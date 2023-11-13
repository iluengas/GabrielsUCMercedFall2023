SELECT r_name, SUM(w_capacity)
FROM nation, region, warehouse
    WHERE n_name = 'SAUDI ARABIA' AND 
        n_regionkey = r_regionkey AND 
        n_nationkey = w_nationkey
        GROUP BY r_regionkey;
