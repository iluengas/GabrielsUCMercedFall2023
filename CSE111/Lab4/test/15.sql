.headers on

SELECT r_name as region, s_name as supplier, MAX(s_acctbal) as acctBal
FROM supplier, nation, region
WHERE s_nationkey = n_nationkey AND    
        n_regionkey = r_regionkey
    GROUP BY r_name;

