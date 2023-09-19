.headers on

SELECT l_shipdate, l_commitdate
FROM lineitem
WHERE 
     l_shipdate < l_commitdate