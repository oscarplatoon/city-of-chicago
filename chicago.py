# Your code goes here!


import csv
import psycopg2
import os

def drop_properties_table():
    return ("DROP TABLE IF EXISTS employees CASCADE;")
    
# Table creation, revisit if varchar fields are broken.
def table_creation_query():
    return ("CREATE TABLE employees (id serial PRIMARY KEY, first_name varchar(255), last_name varchar(255), job_title varchar(60), full_or_part_time varchar, department varchar(255), annual_salary int);")

def clean_data(csv_row):
    cleaned = {}
    # first_name
    # last_name
    ### data comes in as name row['name'] = "Last,  First MI"
    last_first = csv_row['name'].split(",").trim()
    first = last_first[1].split(' ')[0] #this discards Middle Initial
    cleaned['last_name'] = last_first[0]
    cleaned['first_name'] = first
    # job_title
    cleaned['job_title'] =csv_row['Job Titles']
    # full_or_part_time "P/F"
    cleaned['full_or_part_time'] = csv_row['Full or Part-Time']
    # department "str"
    cleaned['department'] = csv_row['Department']
    # annual salary
    ### has to catch hourly vs salary, 
    if csv_row['Salary or Hourly']== 'Hourly':
        hourly_annual = 0
    ### and convert hourly to salary via:
    ### hours_per_week * hourly_rate * 50 to int
        hourly_annual = int(float(csv_row['Typical Hours']) * float(csv_row['Hourly Rate'])* float(50))
        cleaned['annual_salary'] = hourly_annual
    else:
        cleaned['annual_salary'] = csv_row['Annual Salary']

    ## From sac real estate exercise.
    # cleaned['street_address'] = csv_row['street']
    # cleaned['city'] = csv_row['city']
    # cleaned['zip_code'] = csv_row['zip']
    # cleaned['state'] = csv_row['state']
    # cleaned['number_of_beds'] = int(csv_row['beds'])
    # cleaned['number_of_baths'] = int(csv_row['baths'])
    # cleaned['square_feet'] = int(csv_row['sq__ft'])
    # cleaned['property_type'] = csv_row['type']
    # cleaned['sale_date'] = datetime.strptime(csv_row['sale_date'], '%m/%d/%y')
    # cleaned['sale_price'] = csv_row['price']
    # cleaned['latitude'] = Decimal(csv_row['latitude'])
    # cleaned['longitude'] = Decimal(csv_row['longitude'])
    return cleaned


connection = psycopg2.connect(
    f"dbname=chicago_salaries user={os.getlogin()}")
print("Connected!")
cursor = connection.cursor()
cursor.execute(drop_properties_table())
print("Dropped Table!")
cursor.execute(table_creation_query())
print("Created Table")