.headers on

SELECT sum(c_acctbal) as totalActBal 
FROM customer, nation
WHERE customer.c_nationkey = 24 AND 
        customer.c_mktsegment = 'FURNITURE';