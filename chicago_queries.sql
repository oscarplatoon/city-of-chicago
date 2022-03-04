-- Write your Queries here

--Find the employee being paid the most

select * from employees
order by annual_salary::float desc limit 1;

--Find the employee being paid the least
select * from employees
order by annual_salary::float limit 1;

--Find the department with the highest average salary
select department, avg(annual_salary::float) from employees
group by department
order by avg(annual_salary::float) desc limit 1;


--Find the department with the lowest average salary
select department, avg(annual_salary::float) from employees
group by department
order by avg(annual_salary::float) limit 1;

--Find the average salary difference between full time and part time workers

select avg(e1.annual_salary::float) - (select avg(e2.annual_salary::float) 
                                        from employees as e2
                                        where full_or_part_time = 'P')  
from employees as e1
where full_or_part_time = 'F';


--Find the most common first name
select first_name, count(first_name) from employees
group by first_name
order by count(first_name) desc limit 1;


--Find the most common last name
select last_name, count(first_name) from employees
group by last_name
order by count(last_name) desc limit 1;

--If there are people with the same name, find what their job titles, departments, and annual salaries are

select a.id,a.first_name,a.last_name,a.job_title,a.department,a.annual_salary from employees as a
join employees as b on (a.first_name = b.first_name and a.last_name = b.last_name and not a.id = b.id)
group by a.id
order by id;



