-- ## Release 3: Queries
-- Now that we have a database full of employees and their salaries, let's query our database:
-- 2. Find the employee being paid the least
-- --
-- 1. Find the employee being paid the most
Select employees.first_name,
    employees.last_name,
    max(employees.annual_salary)
from employees
group by employees.first_name,
    employees.last_name
order by max(employees.annual_salary) desc
limit 1;

-- 2. Find the employee being paid the least
Select employees.first_name,
    employees.last_name,
    max(employees.annual_salary)
from employees
group by employees.first_name,
    employees.last_name
order by max(employees.annual_salary) asc
limit 1;

-- 3. Find the department with the highest average salary
select employees.department,
    avg(employees.annual_salary)::decimal(12, 2)
from employees
group by employees.department
order by avg(employees.annual_salary) desc
limit 1;

-- 4. Find the department with the lowest average salary
select employees.department,
    avg(employees.annual_salary)::decimal(12, 2)
from employees
group by employees.department
order by avg(employees.annual_salary) asc
limit 1;

-- 5. Find the average salary difference between full time and part time workers

-- Multi select statement for comparator?
-- Avg full time salary:
select avg(employees.annual_salary)
from employees
where full_or_part_time = 'F';

-- Avg part time salaary:
select avg(employees.annual_salary)
from employees
where full_or_part_time = 'P';

-- The comparison
select (
        (
            select avg(employees.annual_salary)
            from employees
            where full_or_part_time = 'F'
        ) - (
            select avg(employees.annual_salary)
            from employees
            where full_or_part_time = 'P'
        )
    )::decimal(12, 2) as "Full time vs Part Time Average Salary Difference";


-- 6. Find the most common first name
select employees.first_name,
    count(employees.first_name)
from employees
group by employees.first_name
order by count(employees.first_name) desc
limit 1;

-- 7. Find the most common last name
select employees.last_name,
    count(employees.last_name)
from employees
group by employees.last_name
order by count(employees.last_name) desc
limit 1;

-- 8. If there are people with the same name, find what their job titles, departments, and annual salaries are

select S.first_name,
    S.last_name,
    S.job_title,
    S.full_or_part_time,
    S.annual_salary,
    S.id
from employees S
    inner join (
            select E.first_name,
                E.last_name
            from employees E
        group by E.first_name,
            E.last_name
        having count(E.first_name || E.last_name) > 1
    ) as M ON
    S.first_name = M.first_name
    AND S.last_name = M.last_name;
