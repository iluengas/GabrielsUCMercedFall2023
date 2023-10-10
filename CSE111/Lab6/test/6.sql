.headers on
-- 6. Find how many suppliers from PERU supply more than 40 different parts.

SELECT COUNT(s_suppkey) as suppliers_cnt
FROM 
(
    SELECT ps_suppkey as suppKey
    FROM partsupp, supplier, nation
    WHERE ps_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                n_name == 'PERU'
                GROUP BY ps_suppkey 
                    HAVING COUNT(ps_suppkey) > 40
), supplier
WHERE suppKey = s_suppkey;