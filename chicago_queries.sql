-- Write your Queries here
--1. Find the employee being paid the most
select * from employees
where annual_salary = (SELECT max(annual_salary) from employees);

--2. Find the employee being paid the least
select * from employees
where annual_salary = (SELECT min(annual_salary) from employees);

--3. Find the department with the highest average salary

select department,avg(annual_salary) from employees
group by department
ORDER BY avg(annual_salary)  desc limit 1;



--4. Find the department with the lowest average salary

select department,avg(annual_salary) from employees
group by department
ORDER BY avg(annual_salary) limit 1;

--5. Find the average salary difference between full time and part time workers


SELECT 
(select avg(annual_salary) from employees where full_or_part_time = 'F')
-
(SELECT avg(annual_salary) from employees where full_or_part_time = 'P')
AS "F/P Time Salary difference";




--6. Find the most common first name

select mode() within group(order by first_name) as "Most common first name" from employees;

--7. Find the most common last name
select mode() within group(order by last_name) as "Most common last name" from employees;

--8. If there are people with the same name, find what their job titles, departments, and annual salaries are

select * from employees as e1
where exists (
    select * from employees as e2
    where e1. first_name =e2.first_name 
    and e1.last_name = e2.last_name
    and e1.id <> e2.id
)
order by first_name, last_name;
