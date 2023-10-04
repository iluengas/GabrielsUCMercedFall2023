.headers on

-- Based on the available quantity of items,
--  who is the manufacturer p mfgr of the most popular item
-- (the more popular an item is, the less available it is in ps availqty)
--  from Supplier#000000040?


SELECT p_mfgr as manufacturer 
FROM supplier, partsupp, part, 
( 
    SELECT MIN(ps_availqty) as min
    FROM partsupp
)
WHERE s_suppkey = ps_suppkey AND 
        ps_partkey = p_partkey AND 
            ps_availqty = min;