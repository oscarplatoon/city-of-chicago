import csv
import os.path
import psycopg2
import ipdb

my_path = os.path.abspath(os.path.dirname(__file__))
chicago_path = os.path.join(my_path, "./data/Current_Employee_Names__Salaries__and_Position_Titles.csv")

with open(chicago_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ipdb.set_trace()
