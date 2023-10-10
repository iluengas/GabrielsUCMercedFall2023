.headers on
-- 4. Find the nation(s) with the least developed industry,
--  i.e., selling items totaling the smallest amount of money (l extendedprice) in 1994 (l shipdate)

SELECT n_name as country
FROM nation, 
(
    SELECT nameKey, MIN(sums)
    FROM 
    (
        SELECT n_name as nameKey, SUM(l_extendedprice) as sums
        FROM lineitem, supplier, nation
        WHERE strftime('%Y', l_shipdate) = '1994' AND 
                l_suppkey = s_suppkey AND 
                    s_nationkey = n_nationkey
                        GROUP BY n_name
    )
)
WHERE nameKey = n_name;

