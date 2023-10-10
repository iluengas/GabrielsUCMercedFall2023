.headers on
-- 8. Find how many suppliers have
--less than 50 distinct orders from customers in EGYPT and JORDAN together.

SELECT c_custkey
FROM customer, nation
WHERE c_nationkey = n_nationkey AND 
        n_name IN ('EGYPT', 'JORDAN');

SELECT * 
FROM orders, lineitem, supplier, 
(
    SELECT c_custkey as custKey
    FROM customer, nation
    WHERE c_nationkey = n_nationkey AND 
            n_name IN ('EGYPT', 'JORDAN')
)
WHERE custKey = o_custkey AND 
        o_orderkey = l_orderkey AND 
            l_suppkey = s_suppkey;