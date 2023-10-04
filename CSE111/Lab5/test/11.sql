.headers on
-- What is the total supply cost (ps supplycost)
--  for parts less expensive than $2000 (p retailprice)
--   shipped in 1994 (l shipdate) by suppliers who did not supply any line item
--    with an extended price less than 1000 in 1997?

-- SELECT DISTINCT s_suppkey as sq_SupKey
-- FROM supplier, lineitem
-- WHERE s_suppkey = l_suppkey AND 
--         l_extendedprice >= 100 AND 
--             substr(l_receiptdate, 1, 4) = '1997';

SELECT TOTAL(ps_supplycost)
FROM (
    SELECT DISTINCT s_suppkey as sq_supKey
    FROM supplier, lineitem
    WHERE s_suppkey = l_suppkey AND 
        l_extendedprice >= 100 AND 
            substr(l_receiptdate, 1, 4) = '1997'
), supplier, partsupp, part, lineitem
WHERE
        s_suppkey = ps_suppkey AND 
            ps_partkey = p_partkey AND 
                p_retailprice < 2000 AND 
                    substr(l_shipdate, 1, 4) = '1994' AND 
                        sq_supKey = s_suppkey;

