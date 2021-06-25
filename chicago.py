# Your code goes here!
import psycopg2
import os
import csv
from decimal import Decimal





def table_creation_query():
    return 'CREATE TABLE employees(first_name varchar,last_name varchar, job_title varchar, full_or_part_time char(1), department varchar, annual_salary money)';

def cleaned_data(csv_row):
    cleaned = {}
    #  annual_salary. **Note**: If an employee is an hourly employee, calculate their annual salary by this equation: `hours_per_week * hourly_salary * 50` (50 weeks a year)
    clean_list = csv_row['Name'].split(',  ')
    cleaned['first_name'] = clean_list[1]
    cleaned['last_name'] = clean_list[0]
    cleaned['job_title'] = csv_row['Job Titles']
    cleaned['full_or_part_time'] = csv_row['Full or Part-Time']
    cleaned['department'] = csv_row['Department']

    clean_hourly_or_salary =  csv_row['Salary or Hourly']
    if clean_hourly_or_salary == 'Hourly':
        horly_salary = Decimal(csv_row['Hourly Rate'])
        hours_per_week = int(csv_row['Typical Hours'])
        cleaned['annual_salary'] = hours_per_week * horly_salary * 50
    else: 
        cleaned['annual_salary'] = Decimal(csv_row['Annual Salary'])
    
    return cleaned

connection = psycopg2.connect(f"dbname=chicago_salaries user={os.getlogin()}")
cursor = connection.cursor()

try:
    cursor.execute(table_creation_query())
    print('success!!')
except:
    print('FAILED ON data creation!!')


with open('data/Current_Employee_Names__Salaries__and_Position_Titles.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        clean_data = cleaned_data(row)
        cursor.execute('INSERT INTO employees(first_name,last_name, job_title, full_or_part_time, department, annual_salary) VALUES (%s, %s, %s, %s, %s,%s);', (clean_data['first_name'],clean_data['last_name'],clean_data['job_title'],clean_data['full_or_part_time'],clean_data['department'],clean_data['annual_salary']))


connection.commit()
connection.close()

#csv file row
# {'Name':  S'WILLIAMS, ETH', 'Job Titles': 'GENERAL LABORER - DSS', 'Department': 'STREETS & SAN', 'Full or Part-Time': 'F', 'Salary or Hourly': 'Hourly', 'Typical Hours': '40', 'Annual Salary': '', 'Hourly Rate': '23.05'}