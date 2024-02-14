from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
data_filepath = 'data/top_50_films.csv.py'
db_name = 'data/Movies.db'
table_name = 'Top_50'

res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
tableRows = soup.find('table').tbody.find_all('tr')
df = pd.DataFrame(columns=['Average Rank', 'Film', 'Year'])

rowCounter = 0
for tr in tableRows:
    if rowCounter > 0:
        values = tr.find_all('td')
        dataDict = {
            'Average Rank': values[0].text,
            'Film': values[1].text,
            'Year': values[2].text
        }
        df1 = pd.DataFrame(dataDict, index=[0])
        df = pd.concat([df, df1], ignore_index=True)

    rowCounter += 1

df.to_csv(data_filepath)

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()