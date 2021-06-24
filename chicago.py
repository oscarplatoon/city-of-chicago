# Your code goes here!
import csv
import psycopg2
import os
import ipdb
from decimal import Decimal
from datetime import datetime

def table_creation_query():
    pass

def split_name(csv_row):
    csv_row[0].split(",") 


def clean_data(csv_row):
    cleaned = {}
    cleaned['first_name'] = csv_row['first_name']
    cleaned['last_name'] = csv_row['last_name']
    cleaned['job_title'] = csv_row['job_title']
    cleaned['full_or_part_time'] = csv_row['full_or_part_time']
    cleaned['department'] = csv_row['department']
    if cleaned['full_or_part_time'] == 'Salary':
        cleaned['annual_salary'] = int(csv_row['annual_salary'])
    else:
        
        return cleaned


with open (Current_Employees_Names__Salaries__and_Position_Titles.csv) as csv_file:
    writer = csv.writer(csv_file)
    for csv_row in writer:
        print(split_name())
        