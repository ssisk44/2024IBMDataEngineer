import pandas as pd
import sqlite3

db_name = 'data/Movies.db'
table_name = 'Top_50'

conn = sqlite3.connect(db_name)

### writing to sql
# df.to_sql(table_name, conn, if_exists = 'replace', index = False)

### querying sql
query = "select * from Top_50"
df = pd.read_sql(query, conn)
print(df)