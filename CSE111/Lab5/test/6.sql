.headers on

-- For parts whose type contains STEEL,
-- return the name of the supplier from AMERICA
-- that can supply them at maximum cost (ps supplycost),
-- for every part size. Print the supplier name together with
-- the part size and the maximum cost.

SELECT s_name, p_size, sq.ps_supplycost 
FROM supplier, partsupp, part, nation, region, 
(
    SELECT ps_partkey as key1, MAX(ps_supplycost) as max
    FROM partsupp
    GROUP BY ps_partkey;
) as sq
WHERE s_suppkey = ps_suppkey AND 
        ps_partkey = p_partkey AND
            p_partkey = sq. 
            s_nationkey = n_nationkey AND
                n_regionkey = r_regionkey AND
                    r_name = 'AMERICA' AND 
                    p_type LIKE '%STEEL' AND 
                        p_partkey = sq.ps_partkey; 


-- SELECT ps_partkey, MAX(ps_supplycost)
-- FROM partsupp
-- GROUP BY ps_partkey;
    
