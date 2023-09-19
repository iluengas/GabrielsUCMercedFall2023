.headers on

SELECT supplier.s_name ,supplier.s_acctbal
FROM supplier, nation
WHERE supplier.s_nationkey = nation.n_nationkey AND
        nation.n_regionkey = 2 AND
        supplier.s_acctbal > 5000;
