.headers on
-- 9. Find how many suppliers supply the least expensive part (p retailprice).


SELECT COUNT(ps_suppkey) as supplier_cnt
FROM (
    SELECT p_partkey as partKey, MIN(p_retailprice) 
    FROM part
), partsupp
WHERE partKey = ps_partkey;