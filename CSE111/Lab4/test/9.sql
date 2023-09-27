.headers on

SELECT * 
FROM (
        SELECT n_name,  count(n_name) as cnt
        FROM orders, customer, nation, region
        WHERE (o_orderdate BETWEEN '1993-01-01' AND '1993-12-31') AND
                o_custkey = c_custkey AND
                    c_nationkey = n_nationkey AND  
                        n_regionkey = r_regionkey AND  
                            r_regionkey = 0
                                GROUP BY n_name
    ) as sq
WHERE sq.cnt > 200; --NO ROWS SATISFY THIS CONDITION WITH MY SOLUTION