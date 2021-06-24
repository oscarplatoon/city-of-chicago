# structure of csv file (current_employee_names_salaries_position_titles.csv)
# Name,Job Titles,Department,Full or Part-Time,Salary or Hourly,Typical Hours,Annual Salary,Hourly Rate

#dbase (name=chicago_salaries) schema:
# Table - employees 
#   - first_name
#   - last_name
#   - job_title
#   - full_or_part_time
#   - department
#   - annual_salary. 
#  **Note**: If an employee is an hourly employee, calculate their annual salary by this equation: #`hours_per_week * hourly_salary * 50` (50 weeks a year)
import psycopg2
import getpass
import csv
import re

def clean_employee_data(csv_row):
    cleaned_data = {}
    cleaned_data['job_title'] = csv_row['Job Titles']
    cleaned_data['department'] = csv_row['Department']
    name_list = csv_row['Name'].split(',  ')
    cleaned_data['last_name'] = name_list[0]
    name_list[1] = re.sub(r' .*', '', name_list[1]) # regex ignore anything after the space
    cleaned_data['first_name'] = name_list[1]
    cleaned_data['full_or_part_time'] = csv_row['Full or Part-Time']
 # fix this to always show exactly 2 decimals places
    if csv_row['Salary or Hourly'] == 'Salary':
        cleaned_data['annual_salary'] = round(float(csv_row['Annual Salary']), 4)
    else:
        cleaned_data['annual_salary'] = round(float(csv_row['Typical Hours']) * float(csv_row['Hourly Rate']), 4)
   
    return cleaned_data


try:
    conn = psycopg2.connect(f"dbname=chicago_salaries user={getpass.getuser()}")
except:
    print("Error connnecting to database.")
    quit()
else:
    print("Connected to database.")

try:
    cur = conn.cursor()
except:
    print("Unable to create a cursor")
    quit()
else:
    print("Cursor created")

try:
    cur.execute("DROP TABLE IF EXISTS employees CASCADE;")
   # come back and make these NOT NULL
    cur.execute("CREATE TABLE employees (id serial PRIMARY KEY, first_name varchar(64), last_name varchar(64), job_title varchar(64), full_or_part_time varchar(16), department varchar(64), annual_salary float);")
    conn.commit()
except:
    print("Unable to create table")
else:
    print("Table employees created")

try:
    with open('Current_Employee_Names__Salaries__and_Position_Titles.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cleaned_data = clean_employee_data(row)
            #cursor.execute("INSERT INTO properties (street_address, city, zip_code, state, number_of_beds, number_of_baths, square_feet, property_type, sale_date, sale_price, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (cleaned_data['street_address'], cleaned_data['city'], cleaned_data['zip_code'], cleaned_data['state'], cleaned_data['number_of_beds'], cleaned_data['number_of_baths'], cleaned_data['square_feet'], cleaned_data['property_type'], cleaned_data['sale_date'], cleaned_data['sale_price'], cleaned_data['latitude'], cleaned_data['longitude']))

            cur.execute("INSERT INTO employees (first_name, last_name, job_title, full_or_part_time, department, annual_salary) VALUES (%s, %s, %s, %s, %s, %s)", (cleaned_data['first_name'], cleaned_data['last_name'], cleaned_data['job_title'], cleaned_data['full_or_part_time'], cleaned_data['department'], cleaned_data['annual_salary']))
            

except Exception as e:
    print(e)
    print("Unable to process data.")
    quit()
else:
    print("Data successfully imported")

conn.commit()
conn.close()