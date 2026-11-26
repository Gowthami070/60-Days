create database company_db;
use company_db;
create table employees(
	emp_id int primary key,
	emp_name varchar(50) not null,
	salary decimal(10,2),
	age int,
	dept_id int,
	manager_id int,
	joining_date date,
	city varchar(30)
);
create table departments(
	dept_id  int primary key,
	dept_name varchar(50),
	location varchar(50)
);
create table projects(
	project_id int primary key,
	project_name varchar(50),
	emp_id int,
	budget decimal(12,2)
);

--------------------------------------------------------
Part 1: SQL Basic Queries & Data Manipulation
1. Create the company database and all three tables with appropriate constraints.
2. Insert at least 10 employee records.
3. Insert at least 5 department records.
4. Insert at least 8 project records.
5. Update the salary of employees belonging to the IT department by 10%.
6. Delete employees whose age is below 20.
7. Display employees whose salary is greater than 40,000.
8. Display the distinct cities from the Employees table.
-------------------------------------------------------------
-
- employee details
INSERT INTO Employees VALUES
(101, 'Rahul', 45000, 25, 1, 105, '2022-01-15', 'Hyderabad'),
(102, 'Priya', 55000, 27, 2, 106, '2021-05-20', 'Chennai'),
(103, 'Kiran', 35000, 24, 1, 105, '2023-03-10', 'Hyderabad'),
(104, 'Sneha', 60000, 29, 3, 107, '2020-07-12', 'Bangalore'),
(105, 'Arjun', 80000, 35, 1, NULL, '2018-02-18', 'Hyderabad'),
(106, 'Divya', 75000, 34, 2, NULL, '2019-06-25', 'Chennai'),
(107, 'Vijay', 90000, 38, 3, NULL, '2017-09-30', 'Bangalore'),
(108, 'Anil', 40000, 26, 4, 109, '2022-11-05', 'Mumbai'),
(109, 'Meena', 70000, 32, 4, NULL, '2019-04-14', 'Mumbai'),
(110, 'Suresh', 30000, 23, 5, 109, '2024-01-08', 'Delhi');

-- departments details
INSERT INTO Departments VALUES
(1, 'IT', 'Hyderabad'),
(2, 'HR', 'Chennai'),
(3, 'Finance', 'Bangalore'),
(4, 'Marketing', 'Mumbai'),
(5, 'Sales', 'Delhi');

-- project details
INSERT INTO Projects VALUES
(201, 'Web Development', 101, 500000),
(202, 'AI Chatbot', 102, 750000),
(203, 'Security System', 103, 600000),
(204, 'Payroll System', 104, 400000),
(205, 'Cloud Migration', 105, 900000),
(206, 'HR Management', 106, 350000),
(207, 'Financial Analysis', 107, 650000),
(208, 'Digital Marketing', 108, 300000);


select emp_name,salary from employees where salary > 40000;
select distinct city from employees;






