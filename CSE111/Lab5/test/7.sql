.headers on

-- Print the name of the parts supplied by suppliers from FRANCE
-- that have total value in the top 5% 
--     total values across all the supplied parts.
-- The total value is ps supplycost*ps availqty. Hint: Use
-- the LIMIT keyword with a SELECT subquery

SELECT
p_name 
FROM part, partsupp, supplier, nation
WHERE p_partkey = ps_partkey AND 
        ps_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                n_name = 'FRANCE' AND 
                    ps_supplycost * ps_availqty >= (
                        SELECT min(value)
                        FROM (
                            SELECT ps_supplycost * ps_availqty as VALUE
                            FROM partsupp
                            ORDER BY VALUE DESC
                            limit (SELECT floor(0.05 * COUNT(*)) FROM partsupp
                        )
                    );
                