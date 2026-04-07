-- # Write your MySQL query statement below

SELECT 
    mgr.employee_id,
    mgr.NAME,
    Count(emp.employee_id) AS reports_count,
    Round(Avg(emp.age))    AS average_age
FROM   
    employees emp
JOIN employees mgr ON emp.reports_to = mgr.employee_id
GROUP BY employee_id
ORDER BY employee_id 


-- # self join

-- # why/when do we need self join:
-- # the data has hierachical relationship stored within the same table
-- # a single row can't use the data from a different row
-- # a self join forces db to put two related rows side by side  

-- # what do we get from a self join:
-- # example
-- -- Employees table:
-- -- +-------------+---------+------------+-----+
-- -- | employee_id | name    | reports_to | age |
-- -- +-------------+---------+------------+-----+
-- -- | 9           | Hercy   | null       | 43  |
-- -- | 6           | Alice   | 9          | 41  |
-- -- | 4           | Bob     | 9          | 36  |
-- -- | 2           | Winston | null       | 37  |
-- -- +-------------+---------+------------+-----+
-- # when we do FROM employees emp JOIN employees mgr ON emp.reports_to = mgr.employee_id, we get:
-- -- | employee_id | name  | reports_to | age | employee_id | name  | reports_to | age |
-- -- | ----------- | ----- | ---------- | --- | ----------- | ----- | ---------- | --- |
-- -- | 4           | Bob   | 9          | 36  | 9           | Hercy | null       | 43  |
-- -- | 6           | Alice | 9          | 41  | 9           | Hercy | null       | 43  |

-- # group by manager id will squash the two rows into one bucket with id = 9
-- # since now there are multiple rows in the bucket, we need to deal with different employee ids and ages
-- # for id we use count, for age with use avg