from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

data_filename = 'Countries_by_GDP.json'
db_filename = 'World_Economies.db'
db_table_name = 'Countries_by_GDP'
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
tbody = soup.find_all('tbody')[2]

df = pd.DataFrame(columns=['Country', 'GDP_USD_billion'])

rowCounter = 0
for row in tbody.find_all('tr'):
    if rowCounter > 2:
        values = row.find_all('td')
        country = values[0].a.text
        population = str(values[2].text).replace(",", "")
        try:
            population = int(population)
        except:
            population = int(0)
        df1 = pd.DataFrame({'Country':country, 'GDP_USD_billion':population}, index=[0])
        df = pd.concat([df,df1], ignore_index=True)
    rowCounter += 1


df.to_json(data_filename)

conn = sqlite3.connect(db_filename)
df.to_sql(db_table_name, conn, if_exists='replace', index=False)


# running a query on the database table to display only the entries with more than a 100 billion USD economy
query = f'SELECT Country, GDP_USD_billion from {db_table_name} where GDP_USD_billion > 100'
res = pd.read_sql(query, conn)
print(res)

conn.close()