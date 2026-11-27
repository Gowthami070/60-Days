use company_db;

------------------------------------------------
Part 2: SQL Operators & Filtering
9. Find employees whose salary is between 30,000 and 60,000.
10. Display employees working in IT, HR and Finance departments.
11. Find employees whose names start with 'A'.
12. Find employees whose names contain 'an'.
13. Display employees whose salary is not between 20,000 and 50,000.
14. Find employees whose city is either Hyderabad or Chennai.
15. Display employees whose manager_id is NULL.
---------------------------------------------------------
select emp_name,salary from employees where salary between 30000 and 60000;
SELECT e.*
FROM Employees e
INNER JOIN Departments d
ON e.dept_id = d.dept_id
WHERE d.dept_name IN ('IT', 'HR', 'Finance');
select emp_name from employees where emp_name like 'A%';
select emp_name from employees where emp_name like '%an%';
select emp_name,salary from employees where salary not between 30000 and 60000;
select emp_name,city from employees where city in('Hyderabad','Chennai');
select emp_name,manager_id from employees where manager_id is Null;

