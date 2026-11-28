use company_db;

---------------------------------------------------------
Part 3: Aggregate Functions & Grouping
16. Find the total number of employees in the company.
17. Find the highest, lowest and average salary.
18. Calculate the total salary paid by each department.
19. Find the number of employees working in each city.
20. Display departments having more than 3 employees.
21. Find the average salary of employees in each department.
22. Display departments whose total salary is greater than 1,00,000.
------------------------------------------------------------
select count(emp_id) from employees;
select max(salary) as maximum_salary,min(salary) as minimum_salary,avg(salary) as average_salary from employees;
select dept_id,sum(salary) as total_salary
from employees
group by dept_id;
select city,count(emp_id) from employees
group by city;
select dept_id,count(emp_id) as employee_cnt from employees
group by dept_id
having count(emp_id)>3;
select dept_id,avg(salary) as total_salary from employees
group by dept_id;
select dept_id,sum(salary) as total_salary from employees
group by dept_id
having sum(salary)>100000;
