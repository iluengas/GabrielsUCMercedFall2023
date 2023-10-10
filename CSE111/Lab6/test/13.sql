.headers on
-- 13. Find the nation(s) with the largest number of customers

SELECT n_name as country
FROM nation,
(
    SELECT n_name as name, MAX(counts)
    FROM 
    (
        SELECT n_name, COUNT(n_name) as counts
        FROM customer, nation
        WHERE c_nationkey = n_nationkey
        GROUP BY n_name
    )
)
WHERE n_name = name;