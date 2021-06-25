import psycopg2
import os
import csv

###########################################################################
# Entry 23602 in csv file changed because title was input incorrectly     #
# Removed comma and quotes from title                                     #
###########################################################################

def clean_data(csv_row):
    cleaned = {}
    cleaned['first_name'] = csv_row[1].strip().split(' ')[0].replace("'","")
    cleaned['last_name'] = csv_row[0].strip().replace("'","")
    cleaned['job_title'] = csv_row[2].strip().replace("'","")
    cleaned['full_or_part_time'] = csv_row[4].strip().replace("'","")
    cleaned['department'] = csv_row[3].strip().replace("'","")
    if csv_row[5].strip() == 'Salary':
        cleaned['annual_salary'] = csv_row[7].strip()
    elif csv_row[5].strip()  == 'Hourly':
        cleaned['annual_salary'] = str(float(csv_row[6].strip())*float(csv_row[8].strip())*50)
    else:
        return(print(f'Error with cleaning, csv_row[5] = {csv_row[5]}'))
    return(
        f"'{cleaned['first_name']}'",f"'{cleaned['last_name']}'",f"'{cleaned['job_title']}'",
        f"'{cleaned['full_or_part_time']}'",f"'{cleaned['department']}'",f"'{cleaned['annual_salary']}'"
        )

try:
    #connect to database
    connection = psycopg2.connect(f"dbname=chicago_salaries user={os.getlogin()}")
    #Create a cursor to interact with database
    cursor = connection.cursor()
except:
    print('Error with connection')
else:
    print('Success!')
    #create employees table
    insert_employee = "insert into employees(first_name,last_name,job_title,full_or_part_time,department,annual_salary) values (%s,%s,%s,%s,%s,%s)"
    drop_employees_table = "drop table if exists employees cascade"
    create_employees_table = "create table employees (id serial primary key, first_name varchar(255) not null, last_name varchar(255) not null, job_title varchar(255) not null, full_or_part_time varchar(1) not null, department varchar(255), annual_salary varchar(255) not null)"

    cursor.execute(drop_employees_table)
    cursor.execute(create_employees_table)
    connection.commit()

try:
    
    data = []
    columns = []
    with open('Current_Employee_Names__Salaries__and_Position_Titles.csv') as csv_file:
        csv_reader= csv.reader(csv_file,delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count +=1
                continue
            else:
                cursor.execute((insert_employee)%(clean_data(", ".join(row).split(','))) )
                connection.commit()
                #cursor.execute((insert_employee)%(clean_data(", ".join(row).split(','))) )
except: 
    print('Error loading data')
else:
    print('Success')









