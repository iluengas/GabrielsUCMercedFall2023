.headers on
-- How many suppliers in every region have more balance in their account than
--  the average account balance of their own region?

SELECT r_name as region, COUNT(s_suppkey) as supp_cnt
FROM supplier, nation, region, 
(
    SELECT r_name as nm, AVG(s_acctbal) regionAvgBal
    FROM supplier, nation, region
    WHERE s_nationkey = n_nationkey AND 
            n_regionkey = r_regionkey
                GROUP BY r_name
) as sq
WHERE s_nationkey = n_nationkey AND 
        n_regionkey = r_regionkey AND 
            r_name = nm AND 
                s_acctbal > regionAvgBal
                    GROUP BY r_name;