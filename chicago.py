import psycopg2
import getpass
import os.path
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
chicago_path = os.path.join(my_path, "./data/Current_Employee_Names__Salaries__and_Position_Titles.csv")

def table_creation_query():
    return "CREATE TABLE employees (id serial PRIMARY KEY, first_name varchar, last_name varchar, job_title varchar, full_or_part_time varchar, department varchar, annual_salary integer);"


def clean_data(csv_row):
    cleaned = {}
    cleaned['first_name'] = csv_row['Name']
    cleaned['last_name'] = csv_row['Name']
    cleaned['job_title'] = csv_row['Job Titles']
    cleaned['full_or_part_time'] = csv_row['Full or Part-Time']
    cleaned['department'] = csv_row['Department']
    
    # Need an if statement to check if an employee is hourly or salary
    # Use the equation to plug in a new value
    # check = csv_row['Salary or Hourly']
    # if check == 'Hourly':
        
    # else:
    # cleaned['annual_salary'] = csv_row['']

    return cleaned

connection = psycopg2.connect(f"dbname=chicago_salaries user={getpass.getuser()}")
cursor = connection.cursor()
cursor.execute(table_creation_query())

with open(chicago_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cleaned_data = clean_data(row)
        cursor.execute("INSERT INTO employees (first_name, last_name, job_title, full_or_part_time, department, annual_salary) VALUES (%s, %s, %s, %s, %s, %s)", (cleaned_data['first_name'], cleaned_data['last_name'], cleaned_data['job_title'], cleaned_data['full_or_part_time'], cleaned_data['department'], cleaned_data['annual_salary']))

connection.commit()
connection.close()


