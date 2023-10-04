.headers on

-- Find the highest value line item(s):
--      (l_extendedprice*(1-l_discount)) 
--         shipped after October 2, 1993. 
-- Print the name of the part corresponding to these line item(s).

SELECT p_name as part
FROM lineitem, 
(
    SELECT MAX(l_extendedprice*(1-l_discount)) as max
    FROM lineitem 
), part
WHERE l_shipdate > '1993-10-02' AND 
        (l_extendedprice*(1-l_discount)) = max AND
            l_partkey = p_partkey;

