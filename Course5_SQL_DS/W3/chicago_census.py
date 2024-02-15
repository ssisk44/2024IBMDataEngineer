import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

conn = sqlite3.connect('chicago_census.db')

tablename = 'chicago_socioeconomic_data'
df = pd.read_csv('chicago_census_data.csv', index_col=None)
df.to_sql(name=tablename, con=conn, if_exists='replace', index=False)

# print(df.columns)
# res = pd.read_sql(f'select count(*) from {tablename} where `HARDSHIP INDEX` > 50.0', conn)
# res = pd.read_sql(f'select max(`HARDSHIP INDEX`) from {tablename}', conn)
# res = pd.read_sql(f'select `COMMUNITY AREA NAME`,max(`HARDSHIP INDEX`) from {tablename}', conn)
# res = pd.read_sql(f'select * from {tablename} where `PER CAPITA INCOME ` > 60000', conn)


sns.jointplot(data=df, x='PER CAPITA INCOME ', y='HARDSHIP INDEX')
# sns.swarmplot(data=df, x='PER CAPITA INCOME ', y='HARDSHIP INDEX')
plt.show()

print(df.describe())
