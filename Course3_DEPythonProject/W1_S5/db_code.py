from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

db_name = 'STAFF.db'
db_table_name = 'Instructors'
data_filename = 'INSTRUCTOR.csv'

conn = sqlite3.connect(db_name)
df = pd.read_csv(data_filename, names=['ID', 'First Name', 'Last Name', 'City', "Country"])
df.to_sql(db_table_name, conn, if_exists='replace', index=False)  # replace, append, fail


query_statement = f"SELECT * FROM {db_table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_output)

query_statement = f"SELECT FNAME FROM {db_table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {db_table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_output)