
SELECT AVG(modelCnt)
FROM
    (SELECT COUNT(model) as modelCnt
    FROM Sales
    GROUP BY sale_id, model)