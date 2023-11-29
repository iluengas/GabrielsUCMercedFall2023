-- CREATE VIEW V1(c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, c_nation,c_region) AS
--                     SELECT c_custkey,
--                     c_name, 
--                     c_address, 
--                     c_phone, 
--                     c_acctbal, 
--                     c_mktsegment, 
--                     c_comment, 
--                     n_name,
--                     r_name 
--                         FROM customer, nation, region
--                         WHERE c_nationkey = n_nationkey AND 
--                                     n_regionkey = r_regionkey;

-- SELECT V1.c_nation as country, COUNT(V1.c_custkey) as cnt FROM orders, V1
-- WHERE o_custkey = V1.c_custkey AND
--         V1.c_region = 'EUROPE'
--     GROUP BY V1.c_nation;

-- CREATE VIEW V2(o_orderkey, o_custkey, o_orderstatus,
--                  o_totalprice, o_orderyear, o_orderpriority,
--                   o_clerk, o_shippriority, o_comment) AS
--         SELECT o_orderkey, 
--         o_custkey, 
--         o_orderstatus, 
--         o_totalprice, 
--         strftime('%Y',o_orderdate), 
--         o_orderpriority, 
--         o_clerk, 
--         o_shippriority, 
--         o_comment 
--         from orders;

-- SELECT o_orderkey, 
--         o_custkey, 
--         o_orderstatus, 
--         o_totalprice, 
--         strftime('%Y',o_orderdate), 
--         o_orderpriority, 
--         o_clerk, 
--         o_shippriority, 
--         o_comment 
--         from orders;

-- SELECT V1.c_name as customer, COUNT(*) as cnt
-- FROM V1, V2
-- WHERE V2.o_custkey = V1.c_custkey AND
--         V1.c_nation = 'EGYPT' AND 
--             V2.o_orderyear = '1992'
--             GROUP BY V1.c_name;

-- select c_name as customer, sum(o_totalprice) as total_price
-- from orders, customer, nation
-- where o_custkey = c_custkey
--     and n_nationkey = c_nationkey
--     and n_name = 'ARGENTINA'
--     and o_orderdate like '1996-%'
-- group by c_name;

-- SELECT V1.c_name as customer, sum(V2.o_totalprice) as total_price
-- FROM V1, V2
-- WHERE V2.o_custkey = V1.c_custkey AND 
--         V1.c_nation = 'ARGENTINA' AND 
--         V2.o_orderyear = '1996'
--         GROUP BY V1.c_name;

-- CREATE VIEW V4(s_suppkey,
--                 s_name, 
--                 s_address, 
--                 s_phone, 
--                 s_acctbal, 
--                 s_comment, 
--                 s_nation, 
--                 s_region) AS
-- SELECT s_suppkey, s_name, s_address, s_phone,
--         s_acctbal, s_comment, n_name, r_name
-- FROM supplier, nation, region
-- WHERE s_nationkey = n_nationkey AND 
--         n_regionkey = r_regionkey;

-- SELECT * FROM V4;

-- select s_name as supplier, count(*) as cnt
-- from partsupp, supplier, nation, part
-- where p_partkey = ps_partkey
--     and ps_suppkey = s_suppkey
--     and s_nationkey = n_nationkey
--     and n_name = 'KENYA'
--     and p_container LIKE '%BOX%'
-- group by s_name;

-- SELECT V4.s_name as supplier, COUNT(*) as cnt
-- FROM partsupp, V4, part
-- WHERE ps_suppkey = V4.s_suppkey AND 
--         V4.s_nation = 'KENYA' AND 
--             ps_partkey = p_partkey AND 
--                 p_container LIKE '%BOX%'
--                 GROUP BY V4.s_name;

-- select n_name as country, count(*) as cnt
-- from supplier, nation
-- where s_nationkey = n_nationkey
--     and (n_name = 'ARGENTINA' OR n_name = 'BRAZIL')
-- group by n_name;

-- SELECT V4.s_nation as country, COUNT(*) as cnt
-- FROM V4
-- WHERE (V4.s_nation = 'ARGENTINA' OR
--         V4.s_nation = 'BRAZIL')
--         GROUP BY V4.s_nation;

-- select s_name as supplier, o_orderpriority as priority, count(distinct ps_partkey) as parts
-- from partsupp, orders, lineitem, supplier, nation
-- where l_orderkey = o_orderkey
--     and l_partkey = ps_partkey
--     and l_suppkey = ps_suppkey
--     and ps_suppkey = s_suppkey
--     and s_nationkey = n_nationkey
--     and n_name = 'INDONESIA'
-- group by s_name, o_orderpriority;

-- SELECT V4.s_name as supplier,
--         o_orderpriority as priority,
--              COUNT(DISTINCT ps_partkey) as parts
-- FROM partsupp, orders, lineitem, V4
-- WHERE l_orderkey = o_orderkey AND 
--         l_partkey = ps_partkey AND 
--             l_suppkey = ps_suppkey AND
--                 ps_suppkey = V4.s_suppkey AND 
--                     V4.s_nation = 'INDONESIA'
--         GROUP BY V4.s_name, o_orderpriority;

-- select n_name as country, o_orderstatus as status, count(*) as orders
-- from orders, customer, nation, region
-- where o_custkey = c_custkey
--     and c_nationkey = n_nationkey
--     and n_regionkey = r_regionkey
--     and r_name='AFRICA'
-- group by n_name, o_orderstatus;

-- SELECT V1.c_nation as country, 
--             V2.o_orderstatus as status,
--                 COUNT(*) as orders
-- FROM V2, V1
-- WHERE V2.o_custkey = V1.c_custkey AND 
--         V1.c_region = 'AFRICA'
--         GROUP BY V1.c_nation, V2.o_orderstatus;

-- select count(distinct o_clerk) as clerks
-- from orders, supplier, nation, lineitem
-- where o_orderkey = l_orderkey
--     and l_suppkey = s_suppkey
--     and s_nationkey = n_nationkey
--     and n_name = 'PERU';

-- SELECT COUNT(DISTINCT V2.o_clerk) as clerks
-- FROM V2, lineitem, V4
-- WHERE V2.o_orderkey = l_orderkey AND 
--         l_suppkey = V4.s_suppkey AND 
--         V4.s_nation = 'PERU';

-- select n_name as country, count(distinct l_orderkey) as cnt
-- from orders, nation, supplier, lineitem, region
-- where o_orderkey = l_orderkey
--     and l_suppkey = s_suppkey
--     and s_nationkey = n_nationkey
--     and n_regionkey = r_regionkey
--     and o_orderstatus = 'F'
--     and o_orderdate like '1993-%'
--     and r_name = 'AFRICA'
-- group by n_name
-- having cnt > 200;

-- SELECT V4.s_nation as country, COUNT(DISTINCT l_orderkey) as cnt
-- FROM lineitem, V2, V4
-- WHERE l_orderkey = V2.o_orderkey AND 
--         l_suppkey = V4.s_suppkey AND
--         V2.o_orderstatus = 'F' AND 
--             V2.o_orderyear = '1993' AND 
--             V4.s_region = 'AFRICA'
--             GROUP BY V4.s_nation
--             HAVING cnt > 200;

-- V10(p type, min discount, max discount) that computes the minimum and maximum
-- discount for every type of part. 

-- CREATE VIEW V10(p_type, min_discount, max_discount) AS
-- SELECT p_type, MIN(l_discount), MAX(l_discount)
-- FROM lineitem, part
-- WHERE l_partkey = p_partkey
-- GROUP BY p_type;

-- SELECT p_type, l_discount, count(*)
-- FROM lineitem, part 
-- WHERE l_partkey = p_partkey
-- GROUP BY p_type, l_discount
-- HAVING COUNT(*) > 0; 

-- SELECT p_type, MIN(l_discount), MAX(l_discount)
-- FROM lineitem, part
-- WHERE l_partkey = p_partkey
-- GROUP BY p_type;

-- select p_type as part_type, min(l_discount) as min_disc, max(l_discount) as max_disc
-- from lineitem, part
-- where l_partkey = p_partkey
--     and (p_type like '%ECONOMY%'
--     or p_type like '%COPPER%')
-- group by p_type;

-- SELECT V10.p_type as part_type,
--         V10.min_discount as min_disc,
--         V10.max_discount as max_disc
-- FROM V10 
-- WHERE (V10.p_type like '%ECONOMY%'
--     or V10.p_type like '%COPPER%')
-- group by V10.p_type;

--  V111(c custkey, c name, c nationkey, c acctbal)
--   and V112(s suppkey, s name, s nationkey,s acctbal)
--    that contain the customers with negative balance
--      and the suppliers with positive balance,respectively

-- CREATE VIEW V111(c_custkey, c_name, c_nationkey, c_acctbal) AS
--     SELECT c_custkey, c_name, c_nationkey, c_acctbal
--     FROM customer
--     WHERE c_acctbal < 0;

-- CREATE VIEW V112(s_suppkey, s_name, s_nationkey, s_acctbal) AS
-- SELECT s_suppkey, s_name, s_nationkey, s_acctbal
-- FROM supplier
-- WHERE s_acctbal > 0;

-- select count(distinct l_orderkey) as order_cnt
-- from lineitem, supplier, orders, customer
-- where l_suppkey = s_suppkey
--     and l_orderkey = o_orderkey
--     and o_custkey = c_custkey
--     and c_acctbal < 0
--     and s_acctbal > 0;

-- SELECT COUNT(DISTINCT l_orderkey) as order_cnt
-- FROM lineitem, V112, orders, V111
-- WHERE l_orderkey = o_orderkey AND 
--         o_custkey = V111.c_custkey AND 
--             l_suppkey = V112.s_suppkey;

-- select r_name as region, max(s_acctbal) as max_bal
-- from supplier, nation, region
-- where s_nationkey = n_nationkey
--     and n_regionkey = r_regionkey
-- group by r_name
-- having max_bal > 9000;

-- SELECT V4.s_region as region, MAX(V4.s_acctbal) as  max_bal
-- FROM V4
-- GROUP BY V4.s_region
-- HAVING max_bal > 9000;

-- select r1.r_name as supp_region, r2.r_name as cust_region, min(o_totalprice) as min_price
-- from lineitem, supplier, orders, customer, nation n1, region r1, nation n2, region r2
-- where l_suppkey = s_suppkey
--     and s_nationkey = n1.n_nationkey
--     and n1.n_regionkey = r1.r_regionkey
--     and l_orderkey = o_orderkey
--     and o_custkey = c_custkey
--     and c_nationkey = n2.n_nationkey
--     and n2.n_regionkey = r2.r_regionkey
-- group by r1.r_name, r2.r_name;

-- SELECT V4.s_region as supp_region,
--         V1.c_region as cust_region, 
--         MIN(o_totalprice) as min_price
-- FROM lineitem, V4, V1, orders
-- WHERE l_orderkey = o_orderkey AND 
--         o_custkey = V1.c_custkey AND 
--         l_suppkey = V4.s_suppkey
--         GROUP BY V4.s_region, V1.c_region;

-- select count(*) as items
-- from orders, lineitem, customer, supplier, nation n1, region, nation n2
-- where o_orderkey = l_orderkey
--     and o_custkey = c_custkey
--     and l_suppkey = s_suppkey
--     and s_nationkey = n1.n_nationkey
--     and n1.n_regionkey = r_regionkey
--     and c_nationkey = n2.n_nationkey
--     and r_name = 'ASIA'
--     and n2.n_name = 'KENYA';

-- SELECT COUNT(*) as items
-- FROM lineitem, V1, V2, V4
-- WHERE l_orderkey = V2.o_orderkey AND 
--         V2.o_custkey = V1.c_custkey AND 
--         V1.c_nation = 'KENYA' AND 
--         l_suppkey = V4.s_suppkey AND 
--         V4.s_region = 'ASIA';


select r.r_name as region, s.s_name as supplier, s.s_acctbal as acct_bal
from supplier s, nation n, region r
where s.s_nationkey = n.n_nationkey
        and n.n_regionkey = r.r_regionkey
        and s.s_acctbal = (select max(s1.s_acctbal)
                            from supplier s1, nation n1, region r1
                            where s1.s_nationkey = n1.n_nationkey
                                    and n1.n_regionkey = r1.r_regionkey
                                    and r.r_regionkey = r1.r_regionkey
                    );
SELECT V4.s_region, V4.s_name, V4.s_acctbal
FROM V4 
GROUP BY V4.s_region 
HAVING V4.s_acctbal = MAX(V4.s_acctbal)
ORDER BY V4.s_name ASC;

