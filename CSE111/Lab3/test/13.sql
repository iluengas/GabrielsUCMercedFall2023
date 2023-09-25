.headers on

SELECT supplier.s_name, count(supplier.s_name)
FROM supplier, lineitem
WHERE supplier.s_suppkey = lineitem.l_suppkey AND 
        lineitem.l_discount = 0.1
        GROUP BY s_name;