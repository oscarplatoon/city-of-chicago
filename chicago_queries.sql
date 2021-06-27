select * from employees order by annual_salary desc limit 1;

select * from employees order by annual_salary asc limit 1;

select department, avg(Cast(annual_salary as decimal)) from employees
group by 1
order by 2 desc
limit 1;

select department, avg(Cast(annual_salary as decimal)) from employees
group by 1
order by 2 asc
limit 1;

-- select full_or_part_time, avg(Cast(annual_salary as decimal)) from employees
-- group by 1
-- order by 2 desc;

select avg(Cast(annual_salary as decimal)) - (
	select avg(Cast(annual_salary as decimal))
	from employees
	where full_or_part_time = 'P'
) as salary_difference
from employees
where full_or_part_time = 'F';

select first_name, count(first_name) as occurrences
from employees
group by 1
order by 2 desc
limit 1;

select last_name, count(last_name) as occurrences
from employees
group by 1
order by 2 desc
limit 1;

select * from employees e1
where exists (
	select * from employees e2
	where e1.first_name = e2.first_name
	and e1.last_name = e2.last_name
	and e1.annual_salary <> e2.annual_salary  -- this should be e1.id, but employees.id doesn't exist. surely people with same name won't make the same salary?
)
order by first_name, last_name;