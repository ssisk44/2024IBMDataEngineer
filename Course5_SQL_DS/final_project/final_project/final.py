import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

census_data_fp = './ChicagoCensusData.csv'
census_table_name = 'CENSUS_DATA'

crime_data_fp = './ChicagoCrimeData.csv'
crime_data_table_name = 'CHICAGO_CRIME_DATA'

public_schools_data_fp = './ChicagoPublicSchools.csv'
public_schools_table_name = 'CHICAGO_PUBLIC_SCHOOLS'

conn = sqlite3.connect('final_project.db')
census_df = pd.read_csv(census_data_fp, index_col=None)
crime_df = pd.read_csv(crime_data_fp, index_col=None)
schools_df = pd.read_csv(public_schools_data_fp, index_col=None)

census_df.to_sql(census_table_name, conn, if_exists='replace', index=False)
crime_df.to_sql(crime_data_table_name, conn, if_exists='replace', index=False)
schools_df.to_sql(public_schools_table_name, conn, if_exists='replace', index=False)

# res = conn.execute("select name from sqlite_master where type='table'")
# print(res.fetchall())

#  PROBLEM 1
# p1 = pd.read_sql(sql=f'select count(*) from {crime_data_table_name}', con=conn)
# print(p1)  #533


#  PROBLEM 2
# p2 = pd.read_sql(sql=f'select COMMUNITY_AREA_NUMBER,PER_CAPITA_INCOME from {census_table_name} where PER_CAPITA_INCOME < 11000', con=conn)
# print(p2)


#  # PROBLEM 3
# p3 = pd.read_sql(sql=f"select CASE_NUMBER from {crime_data_table_name} where DESCRIPTION like '%minor%'", con=conn)
# print(p3)

#  PROBLEM 4
# p4 = pd.read_sql(sql=f"select * from {crime_data_table_name} where primary_type = 'KIDNAPPING' and DESCRIPTION like '%child%'", con=conn)
# print(p4)

#  PROBLEM 5
# p5 = pd.read_sql(sql=f"select distinct(primary_type) from {crime_data_table_name} where LOCATION_DESCRIPTION like '%school%'", con=conn)
# print(p5)

#  # PROBLEM 6
# p6 = pd.read_sql(sql=f"select `Elementary, Middle, or High School` as SCHOOL_TYPE, avg(SAFETY_SCORE) from {public_schools_table_name} group by SCHOOL_TYPE", con=conn)
# print(p6)

#  PROBLEM 7
# p7 = pd.read_sql(sql=f"select COMMUNITY_AREA_NAME,PERCENT_HOUSEHOLDS_BELOW_POVERTY from {census_table_name} order by PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC limit 5", con=conn)
# print(p7)

#  PROBLEM 8
# p8 = pd.read_sql(sql=f"select COMMUNITY_AREA_NUMBER, count(*) from {crime_data_table_name} group by COMMUNITY_AREA_NUMBER having COMMUNITY_AREA_NUMBER > 0 order by count(*) DESC", con=conn)
# print(p8)


#  PROBLEM 9
# p9 = pd.read_sql(sql=f"select COMMUNITY_AREA_NAME from {census_table_name} order by HARDSHIP_INDEX DESC", con=conn)
# print(p9)

#  PROBLEM 10
# p10 = pd.read_sql(sql=f"select COMMUNITY_AREA_NAME from {census_table_name} where COMMUNITY_AREA_NUMBER = (SELECT COMMUNITY_AREA_NUMBER from {crime_data_table_name} group by COMMUNITY_AREA_NUMBER order by count(*) DESC)", con=conn)
# print(p10)

conn.close()