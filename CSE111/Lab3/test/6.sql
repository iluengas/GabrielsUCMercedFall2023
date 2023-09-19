.headers on

SELECT n_name, sum(s_acctbal)
FROM supplier, nation
WHERE nation.n_nationkey = s_nationkey
GROUP BY s_nationkey;

