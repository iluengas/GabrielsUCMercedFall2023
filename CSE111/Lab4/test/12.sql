.headers on

SELECT r_name as region, MAX(s_acctbal) as maxBal
FROM supplier, nation, region
WHERE s_nationkey = n_nationkey AND 
        n_regionkey = r_regionkey
GROUP BY r_name
    HAVING MAX(s_acctbal) > 9000;

