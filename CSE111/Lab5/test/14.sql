.headers on
-- The market share for a given nation within a given region is defined as the fraction of the revenue from
-- the line items ordered by customers in the given region that are supplied by suppliers from the given
-- nation. The revenue of a line item is defined as l extendedprice*(1-l discount). Determine the
-- market share of FRANCE in AMERICA in 1994 (l shipdate).

SELECT oRev2/SUM(orderRevenue)
FROM supplier, nation, region,
(
    SELECT l_orderkey as orderKey, SUM(l_extendedprice*(1-l_discount)) as orderRevenue, l_suppkey as suppKey
    FROM lineitem, orders, customer, nation, region, supplier
    WHERE substr(l_shipdate, 1, 4) = '1994' AND
            l_orderkey = o_orderkey AND
                    o_custkey = c_custkey AND 
                        c_nationkey = n_nationkey AND 
                            n_name = 'FRANCE'
    GROUP BY l_orderkey
),
(
    SELECT SUM(l_extendedprice*(1-l_discount)) as oRev2
    FROM lineitem, supplier, nation, region
    WHERE l_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                n_regionkey = r_regionkey AND 
                    r_name = 'AMERICA'
);
