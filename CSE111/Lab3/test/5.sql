.headers on

SELECT l_receiptdate, l_returnflag, l_extendedprice, l_tax
FROM lineitem 
WHERE l_returnflag != 'Y' AND
      l_receiptdate = '1995-09-22';
