.headers on

SELECT min(c_acctbal) as minBalance, 
       max(c_acctbal) as maxBalance,
       sum(c_acctbal) as totBalance
FROM customer
WHERE c_mktsegment = 'FURNITURE';
