-- Write your Queries here
DROP TABLE if EXISTS employees;
CREATE TABLE employees (
  first_name  VARCHAR(255) NOT NULL,
  last_name   VARCHAR(255) NOT NULL,
  job_title   VARCHAR(255) NOT NULL,
  full_or_part_time VARCHAR(255) NOT NULL,
  department VARCHAR(255) NOT NULL,
  annual_salary INTEGER
);