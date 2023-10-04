.headers on
-- --  How many customers from every region have placed
--  at least one order and have more than the average
-- account balance?

SELECT r_name as region, (COUNT(DISTINCT c_custkey)) as cust_cnt
FROM customer,
 ( 
    SELECT DISTINCT c_custkey as custkey, avg as avgBal
    FROM customer, 
    (
        SELECT AVG(c_acctbal) as avg
        FROM customer
    )
    GROUP BY c_custkey
 ), orders, nation, region
WHERE c_custkey = custkey AND
        c_acctbal > avgBal AND 
            c_custkey = o_custkey AND 
                c_nationkey = n_nationkey AND 
                    n_regionkey = r_regionkey
                        GROUP BY r_name;





