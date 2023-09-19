.headers on

SELECT STRFTIME('%Y-%m', lineitem.l_receiptdate) as orderMonth, count(*) as lineItems
FROM orders, customer, lineitem
WHERE orders.o_orderkey = lineitem.l_orderkey AND
        orders.o_custkey = customer.c_custkey AND
        customer.c_name = 'Customer#000000227'
        GROUP BY  STRFTIME('%m', lineitem.l_receiptdate);
