-- SQLite

--1
select n_name as country, count(*) as cnt
from orders, nation, region, customer
where c_custkey = o_custkey
    and c_nationkey = n_nationkey
    and n_regionkey = r_regionkey
    and r_name='EUROPE'
group by n_name;
    
--2
select c_name as customer, count(*) as cnt
from orders, customer, nation
where o_custkey = c_custkey
    and c_nationkey = n_nationkey
    and n_name = 'EGYPT'
    and o_orderdate like '1992-%'
group by c_name;

--3
select c_name as customer, sum(o_totalprice) as total_price
from orders, customer, nation
where o_custkey = c_custkey
    and n_nationkey = c_nationkey
    and n_name = 'ARGENTINA'
    and o_orderdate like '1996-%'
group by c_name;

--4
select s_name as supplier, count(*) as cnt
from partsupp, supplier, nation, part
where p_partkey = ps_partkey
    and ps_suppkey = s_suppkey
    and s_nationkey = n_nationkey
    and n_name = 'KENYA'
    and p_container LIKE '%BOX%'
group by s_name;

--5
select n_name as country, count(*) as cnt
from supplier, nation
where s_nationkey = n_nationkey
    and (n_name = 'ARGENTINA' OR n_name = 'BRAZIL')
group by n_name;

--6
select s_name as supplier, o_orderpriority as priority, count(distinct ps_partkey) as parts
from partsupp, orders, lineitem, supplier, nation
where l_orderkey = o_orderkey
    and l_partkey = ps_partkey
    and l_suppkey = ps_suppkey
    and ps_suppkey = s_suppkey
    and s_nationkey = n_nationkey
    and n_name = 'INDONESIA'
group by s_name, o_orderpriority;

--7
select n_name as country, o_orderstatus as status, count(*) as orders
from orders, customer, nation, region
where o_custkey = c_custkey
    and c_nationkey = n_nationkey
    and n_regionkey = r_regionkey
    and r_name='AFRICA'
group by n_name, o_orderstatus;

--8
select count(distinct o_clerk) as clerks
from orders, supplier, nation, lineitem
where o_orderkey = l_orderkey
    and l_suppkey = s_suppkey
    and s_nationkey = n_nationkey
    and n_name = 'PERU';

--9
select n_name as country, count(distinct l_orderkey) as cnt
from orders, nation, supplier, lineitem, region
where o_orderkey = l_orderkey
    and l_suppkey = s_suppkey
    and s_nationkey = n_nationkey
    and n_regionkey = r_regionkey
    and o_orderstatus = 'F'
    and o_orderdate like '1993-%'
    and r_name = 'AFRICA'
group by n_name
having cnt > 200;

--10
select p_type as part_type, min(l_discount) as min_disc, max(l_discount) as max_disc
from lineitem, part
where l_partkey = p_partkey
    and (p_type like '%ECONOMY%'
    or p_type like '%COPPER%')
group by p_type;

--11
select count(distinct l_orderkey) as order_cnt
from lineitem, supplier, orders, customer
where l_suppkey = s_suppkey
    and l_orderkey = o_orderkey
    and o_custkey = c_custkey
    and c_acctbal < 0
    and s_acctbal > 0;

--12
select r_name as region, max(s_acctbal) as max_bal
from supplier, nation, region
where s_nationkey = n_nationkey
    and n_regionkey = r_regionkey
group by r_name
having max_bal > 9000;

--13
select r1.r_name as supp_region, r2.r_name as cust_region, min(o_totalprice) as min_price
from lineitem, supplier, orders, customer, nation n1, region r1, nation n2, region r2
where l_suppkey = s_suppkey
    and s_nationkey = n1.n_nationkey
    and n1.n_regionkey = r1.r_regionkey
    and l_orderkey = o_orderkey
    and o_custkey = c_custkey
    and c_nationkey = n2.n_nationkey
    and n2.n_regionkey = r2.r_regionkey
group by r1.r_name, r2.r_name;

--14
select count(*) as items
from orders, lineitem, customer, supplier, nation n1, region, nation n2
where o_orderkey = l_orderkey
    and o_custkey = c_custkey
    and l_suppkey = s_suppkey
    and s_nationkey = n1.n_nationkey
    and n1.n_regionkey = r_regionkey
    and c_nationkey = n2.n_nationkey
    and r_name = 'ASIA'
    and n2.n_name = 'KENYA';

--15
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
