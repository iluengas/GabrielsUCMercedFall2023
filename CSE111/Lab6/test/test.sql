-- SELECT ps_suppkey, s_nationkey , SUM(p_size)
-- FROM part, partsupp, supplier
-- WHERE p_partkey = ps_partkey AND 
--         ps_suppkey = s_suppkey
--             GROUP BY ps_suppkey;

SELECT s_nationkey, MAX(sum)
FROM (
SELECT ps_suppkey, s_nationkey , SUM(p_size) as sum
FROM part, partsupp, supplier
WHERE p_partkey = ps_partkey AND 
        ps_suppkey = s_suppkey
            GROUP BY ps_suppkey
)
    GROUP BY s_nationkey;