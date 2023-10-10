.headers on
-- 7. Find the total quantity (l quantity) of line items shipped per month (l shipdate) in 1997.
 --Hint: check function strftime to extract the month/year from a date

 SELECT strftime('%m', l_shipdate) as month, SUM(l_quantity) as tot_month
 FROM lineitem
    WHERE strftime('%Y', l_shipdate) = '1997'
        GROUP BY strftime('%m', l_shipdate); 