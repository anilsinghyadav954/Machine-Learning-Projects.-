-- ============================================================
-- ASSIGNMENT 5 - MYSQL
-- Employee Management and SQL Queries
-- ============================================================

-- Database Selection
USE rrgi;


-- ============================================================
-- TABLE CREATION
-- ============================================================

DROP TABLE IF EXISTS employee_assignment5;

CREATE TABLE employee_assignment5 (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(45),
    emp_age INT,
    emp_department VARCHAR(30),
    emp_salary INT,
    emp_city VARCHAR(45)
);


-- ============================================================
-- INSERT 10 EMPLOYEES
-- ============================================================

INSERT INTO employee_assignment5
VALUES
(101, 'Aditya', 19, 'IT', 60000, 'Delhi'),
(102, 'Aman', 20, 'HR', 65000, 'Delhi'),
(103, 'Arun', 22, 'IT', 68000, 'Lucknow'),
(104, 'Anil', 21, 'CSE', 70000, 'Hydrabad'),
(105, 'Saurabh', 21, 'CSD', 960000, 'Sitapur'),
(106, 'Shivam', 21, 'IT', 899999, 'Jaunpur'),
(107, 'Krishna', 22, 'HR', 78000, 'Lucknow'),
(108, 'Adarsh', 22, 'CSE', 69000, 'Delhi'),
(109, 'Chandan', 21, 'IT', 80000, 'Ballia'),
(110, 'Sunil', 21, 'IT', 90000, 'Jaunpur');


-- ============================================================
-- VERIFY DATA
-- ============================================================

SELECT * FROM employee_assignment5;


-- ============================================================
-- QUESTION 1
-- Find Employee from Sitapur
-- ============================================================

SELECT emp_name
FROM employee_assignment5
WHERE emp_city = 'Sitapur';


-- ============================================================
-- QUESTION 2
-- Update Saurabh's Salary
-- ============================================================

UPDATE employee_assignment5
SET emp_salary = 10000000
WHERE emp_name = 'Saurabh';


-- ============================================================
-- QUESTION 3
-- Update Employee Name
-- ============================================================

UPDATE employee_assignment5
SET emp_name = 'XYZ'
WHERE emp_id = 104;


-- ============================================================
-- QUESTION 4
-- Employees with Salary > 70000
-- ============================================================

SELECT *
FROM employee_assignment5
WHERE emp_salary > 70000;


-- ============================================================
-- QUESTION 5
-- Employees in IT Department
-- ============================================================

SELECT *
FROM employee_assignment5
WHERE emp_department = 'IT';


-- ============================================================
-- QUESTION 6
-- Employees from Lucknow
-- ============================================================

SELECT *
FROM employee_assignment5
WHERE emp_city = 'Lucknow';


-- ============================================================
-- QUESTION 7
-- Salary Between 70000 and 90000
-- ============================================================

SELECT *
FROM employee_assignment5
WHERE emp_salary > 70000
AND emp_salary < 90000;


-- ============================================================
-- QUESTION 8
-- Names Starting with A
-- ============================================================

SELECT *
FROM employee_assignment5
WHERE emp_name LIKE 'A%';


-- ============================================================
-- QUESTION 9
-- Names Ending with a
-- ============================================================

SELECT *
FROM employee_assignment5
WHERE emp_name LIKE '%a';


-- ============================================================
-- QUESTION 10
-- Employees in IT or HR
-- ============================================================

SELECT *
FROM employee_assignment5
WHERE emp_department = 'IT'
OR emp_department = 'HR';


-- ============================================================
-- QUESTION 11
-- Age > 21 and Salary > 70000
-- ============================================================

SELECT *
FROM employee_assignment5
WHERE emp_age > 21
AND emp_salary > 70000;


-- ============================================================
-- QUESTION 12
-- Delete Employee by ID
-- ============================================================

DELETE FROM employee_assignment5
WHERE emp_id = 110;


-- ============================================================
-- QUESTION 13
-- Delete Employee by Name
-- ============================================================

DELETE FROM employee_assignment5
WHERE emp_name = 'Aditya';


-- ============================================================
-- QUESTION 14
-- Sort Employees by Salary - Ascending
-- ============================================================

SELECT *
FROM employee_assignment5
ORDER BY emp_salary ASC;


-- ============================================================
-- QUESTION 15
-- Sort Employees by Salary - Descending
-- ============================================================

SELECT *
FROM employee_assignment5
ORDER BY emp_salary DESC;


-- ============================================================
-- QUESTION 16
-- Count Employees by Department
-- ============================================================

SELECT
    emp_department,
    COUNT(emp_name) AS employee_count
FROM employee_assignment5
GROUP BY emp_department;


-- ============================================================
-- QUESTION 17
-- Average Salary by Department
-- ============================================================

SELECT
    emp_department,
    AVG(emp_salary) AS avg_salary
FROM employee_assignment5
GROUP BY emp_department;


-- ============================================================
-- QUESTION 18
-- Maximum Salary by Department
-- ============================================================

SELECT
    emp_department,
    MAX(emp_salary) AS max_salary
FROM employee_assignment5
GROUP BY emp_department;


-- ============================================================
-- QUESTION 19
-- Departments Having More Than 2 Employees
-- ============================================================

SELECT emp_department
FROM employee_assignment5
GROUP BY emp_department
HAVING COUNT(emp_name) > 2;


-- ============================================================
-- QUESTION 20
-- Departments with Average Salary > 70000
-- ============================================================

SELECT emp_department
FROM employee_assignment5
GROUP BY emp_department
HAVING AVG(emp_salary) > 70000;


-- ============================================================
-- QUESTION 21
-- Departments Ordered by Average Salary
-- ============================================================

SELECT emp_department
FROM employee_assignment5
GROUP BY emp_department
ORDER BY AVG(emp_salary) ASC;


-- ============================================================
-- QUESTION 22
-- Average Salary by Department - Named Column
-- ============================================================

SELECT
    emp_department,
    AVG(emp_salary) AS avg_salary
FROM employee_assignment5
GROUP BY emp_department
ORDER BY AVG(emp_salary) ASC;


-- ============================================================
-- QUESTION 23
-- Number of Employees by City
-- ============================================================

SELECT
    emp_city,
    COUNT(emp_name) AS Number_Of_emp
FROM employee_assignment5
GROUP BY emp_city;


-- ============================================================
-- QUESTION 24
-- Cities Having More Than 1 Employee
-- ============================================================

SELECT emp_city
FROM employee_assignment5
GROUP BY emp_city
HAVING COUNT(emp_name) > 1;


-- ============================================================
-- QUESTION 25
-- Final Verification
-- ============================================================

SELECT * FROM employee_assignment5;

DESC employee_assignment5;

SHOW TABLES;


-- ============================================================
-- END OF ASSIGNMENT 5
-- ============================================================