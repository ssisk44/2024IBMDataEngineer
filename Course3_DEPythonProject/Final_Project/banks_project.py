### FINAL PROJECT ###
import sqlite3

import pandas as pd
import requests
from datetime import datetime

from bs4 import BeautifulSoup

data_url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
exchange_rate_filepath = 'exchange_rate.csv'
data_output_filepath = 'Largest_banks_data.csv'
db_filename = 'Banks.db'
db_table_name = 'Largest_banks'
log_filename = 'code_log.txt'

def main():
    log_progress("Preliminaries complete. Initiating ETL process")

    extracted_data = extract(data_url, ['Name', 'MC_USD_Billion'])
    log_progress("Data extraction complete. Initiating Transformation process")

    transformed_data = transform(extracted_data, exchange_rate_filepath)
    log_progress("Data transformation complete. Initiating Loading process")

    load_to_csv(transformed_data, data_output_filepath)
    log_progress("Data saved to CSV file")

    conn = sqlite3.connect(db_filename)
    log_progress("SQL Connection initiated")

    load_to_db(transformed_data, conn, 'Largest_banks')
    log_progress("Data loaded to Database as a table, Executing queries")

    query_statement_1 = "SELECT * FROM Largest_banks"
    run_query(query_statement_1, conn)
    query_statement_2 = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
    run_query(query_statement_2, conn)
    query_statement_3 = "SELECT Name from Largest_banks LIMIT 5"
    run_query(query_statement_3, conn)
    log_progress("Process Complete")

    conn.close()
    log_progress("Server Connection closed")


def log_progress(message: str):
    with open(log_filename, 'a') as file:
        timestamp_format = '%Y-%h-%d-%H:%M:%S'
        timestamp = datetime.now().strftime(timestamp_format)
        file.write("<" + timestamp + '> : <' + message + '>\n')

def extract(url, table_attribs):
    df = pd.DataFrame(columns=table_attribs)
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    tbody = soup.find('tbody')

    rowCounter = 0
    for tr in tbody.find_all('tr'):
        if rowCounter > 0:
            tds = tr.find_all('td')
            name = [x.text for x in tds[1].children][2]
            market_cap = float(tds[2].text[:-1])
            df1 = pd.DataFrame({'Name':name, 'MC_USD_Billion':market_cap}, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
        rowCounter += 1

    return df

def transform(df, csv_path):
    exchange_rate_df = pd.read_csv(csv_path)
    for index,row in exchange_rate_df.iterrows():
        df[f"MC_{row[0]}_Billion"] = round(df["MC_USD_Billion"] * float(row[1]), 2)
    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    res = pd.read_sql(query_statement, sql_connection)
    print(str(query_statement) + " -->\n" + str(res) + "\n\n")






main()



