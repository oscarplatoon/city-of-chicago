import psycopg2
import os
import csv
from decimal import Decimal


def create_table_employees():
    return """
            drop table if exists employees;
			create table employees (
				first_name varchar(255) not null,
				last_name varchar(255) not null,
				job_title varchar(255) not null,
				full_or_part_time char(1) not null,
				department varchar(255) not null,
				annual_salary money not null	
			);
		"""


def clean_row(row):
    cleaned_row = {}

    name_arr = row['Name'].split(', ')
    cleaned_row['first_name'] = name_arr[1]
    cleaned_row['last_name'] = name_arr[0]

    cleaned_row['job_title'] = row['Job Titles']
    cleaned_row['full_or_part_time'] = row['Full or Part-Time']
    cleaned_row['department'] = row['Department']

    salary_or_hourly = row['Salary or Hourly']
    if salary_or_hourly == 'Salary':
        annual_salary = Decimal(row['Annual Salary'])
    else:
        annual_salary = int(row['Typical Hours']) * \
            Decimal(row['Hourly Rate']) * 50
    cleaned_row['annual_salary'] = annual_salary

    return cleaned_row


# creating employees tables
conn = psycopg2.connect(f"dbname=chicago_salaries user={os.getlogin()}")

try:
    with conn.cursor() as curs:
        curs.execute(create_table_employees())

        # reading csv file
        dir_path = os.getcwd()
        csv_path = os.path.join(dir_path, "data.csv")
        with open(csv_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cleaned_row = clean_row(row)
                curs.execute(
                    'insert into employees (first_name, last_name, job_title, full_or_part_time, department, annual_salary) values (%s, %s, %s, %s, %s, %s);', (cleaned_row['first_name'], cleaned_row['last_name'], cleaned_row['job_title'], cleaned_row['full_or_part_time'], cleaned_row['department'], cleaned_row['annual_salary']))

        conn.commit()
finally:
    conn.close()
