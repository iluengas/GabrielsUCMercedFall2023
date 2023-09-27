.headers on

SELECT p_type,  MIN(l_discount) as minDisc, MAX(l_discount) as maxDisc
FROM part, lineitem
WHERE
    (p_type LIKE '%COPPER' OR p_type LIKE 'ECONOMY%') AND
    p_partkey = l_partkey
        GROUP BY p_type;

