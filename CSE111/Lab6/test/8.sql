.headers on

SELECT COUNT(*) as supplier_cnt
FROM
(
        SELECT s_suppkey, COUNT(s_suppkey) 
        FROM orders, lineitem, supplier, 
        (
        SELECT c_custkey as custKey
        FROM customer, nation
        WHERE c_nationkey = n_nationkey AND 
                n_name IN ('EGYPT', 'JORDAN')
        )
        WHERE custKey = o_custkey AND 
                o_orderkey = l_orderkey AND 
                l_suppkey = s_suppkey
                GROUP BY s_suppkey 
                        HAVING COUNT(s_suppkey) < 50
);