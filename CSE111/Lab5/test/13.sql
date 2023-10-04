.headers on
-- For any two regions,
--  find the gross discounted revenue (l extendedprice*(1-l discount)) derived
-- from line items in which parts are shipped from a supplier in the first region to a customer in the
-- second region in 1994 and 1995. List the supplier region, the customer region, the year (l shipdate),
-- and the revenue from shipments that took place in that year.
 
 SELECT r1.r_name as supp_region, r2.r_name as cust_region, strftime('%Y', l_shipdate) as year, SUM(l_extendedprice*(1-l_discount)) as revenue
 FROM lineitem, supplier, customer, orders, region r1, region r2, nation n1, nation n2
 WHERE l_suppkey = s_suppkey AND 
            s_nationkey = n1.n_nationkey AND 
                n1.n_regionkey = r1.r_regionkey AND 
                    l_orderkey = o_orderkey AND 
                        o_custkey = c_custkey AND 
                            c_nationkey = n2.n_nationkey AND 
                                n2.n_regionkey = r2.r_regionkey AND
                                    l_shipdate BETWEEN '1994-01-01' AND '1995-12-31'
                                        GROUP BY r1.r_name, r2.r_name, strftime('%Y', l_shipdate);
