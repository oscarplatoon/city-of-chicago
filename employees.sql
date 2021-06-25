-- 1. Find the employee being paid the most
SELECT first_name, max(annual_salary) FROM employees
  GROUP BY first_name
  ORDER by max(annual_salary) desc limit 1;
-- 2. Find the employee being paid the least
SELECT first_name, min(annual_salary) FROM employees
 GROUP BY first_name
 ORDER by min(annual_salary) limit 1;
-- 3. Find the department with the highest average salary
SELECT department, sum(annual_salary)/count(*) FROM employees
  GROUP BY department
  ORDER BY sum(annual_salary)/count(*) desc limit 1;

-- 4. Find the department with the lowest average salary
SELECT department, sum(annual_salary)/count(*) FROM employees
  GROUP BY department
  ORDER BY sum(annual_salary)/count(*) asc limit 1;
-- 5. Find the average salary difference between full time and part time workers
SELECT full_or_part_time, sum(annual_salary)/count(*) FROM employees 
  GROUP BY full_or_part_time;
-- 6. Find the most common first name
SELECT first_name, count(*) FROM employees
  GROUP BY first_name
  ORDER BY count(*) desc limit 1;
-- 7. Find the most common last name
SELECT last_name, count(*) FROM employees
  GROUP BY last_name
  ORDER BY count(*) desc limit 1;
-- 8. If there are people with the same name, find what their job titles, departments, and annual salaries are
SELECT * FROM employees
    WHERE first_name, last_name IN (SELECT first_name, last_name, job_title, department, annual_salary 
                                FROM employees 
                                GROUP BY first_name, last_name 
                                HAVING COUNT(first_name, last_name) > 1);