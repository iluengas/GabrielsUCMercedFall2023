.headers on
-- 12. Find how many parts are supplied by exactly one suppliers from UNITED STATES

SELECT COUNT(partKey) as part_cnt
FROM
(
    SELECT ps_partkey as partKey, COUNT(ps_partkey)
    FROM partsupp, supplier, nation
    WHERE ps_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                n_name == 'UNITED STATES'
                GROUP BY ps_partkey
                    HAVING COUNT(ps_partkey) = 1
);