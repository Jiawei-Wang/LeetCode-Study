-- # Write your MySQL query statement below
delete p1 from person p1, person p2 
where p1.email = p2.email and p1.id > p2.id;

/*
when two tables are listed without any condition
db takes every single row from first table and pairs 
it with every single row from second table
*/