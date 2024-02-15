import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

socioeconomic_data_fp = './ChicagoCensusData.csv'
socioeconomic_table_name = 'CENSUS_DATA'

crime_data_fp = './ChicagoCrimeData.csv'
crime_data_table_name = 'CHICAGO_CRIME_DATA'

public_schools_data_fp = './ChicagoPublicSchools.csv'
public_schools_table_name = 'CHICAGO_PUBLIC_SCHOOLS'

conn = sqlite3.connect('honors_project.db')
census_df = pd.read_csv(socioeconomic_data_fp, index_col=None)
crime_df = pd.read_csv(crime_data_fp, index_col=None)
schools_df = pd.read_csv(public_schools_data_fp, index_col=None)

census_df.to_sql(socioeconomic_table_name, conn, if_exists='replace', index=False)
crime_df.to_sql(crime_data_table_name, conn, if_exists='replace', index=False)
schools_df.to_sql(public_schools_table_name, conn, if_exists='replace', index=False)

### Problem1
# q1_sql = f"select P.NAME_OF_SCHOOL, P.COMMUNITY_AREA_NAME, P.AVERAGE_STUDENT_ATTENDANCE from {public_schools_table_name} P LEFT JOIN {socioeconomic_table_name} E ON P.COMMUNITY_AREA_NUMBER = E.COMMUNITY_AREA_NUMBER WHERE E.HARDSHIP_INDEX = 98;"
# res = pd.read_sql(sql=q1_sql, con=conn)
# print(res)

# ## Problem 2
# q2_sql = f"select C.CASE_NUMBER,C.PRIMARY_TYPE,E.COMMUNITY_AREA_NAME from {crime_data_table_name} C LEFT JOIN {socioeconomic_table_name} E ON C.COMMUNITY_AREA_NUMBER = E.COMMUNITY_AREA_NUMBER where C.LOCATION_DESCRIPTION like '%school%';"
# res = pd.read_sql(sql=q2_sql, con=conn)
# print(res)


### Problem 3
# q3_sql = f"CREATE VIEW chicago_school_info(School_Name,Safety_Rating,Family_Rating,Environment_Rating,Instruction_Rating,Leaders_Rating,Teachers_Rating) AS SELECT NAME_OF_SCHOOL,Safety_Icon,Family_Involvement_Icon,Environment_Icon,Instruction_Icon,Leaders_Icon,Teachers_Icon from {public_schools_table_name};"
# cursor = conn.cursor()
# cursor.execute(q3_sql)
# res = pd.read_sql(sql="select * from chicago_school_info;", con=conn)
# print(res)


### Problem 4

# def update_leaders_score_procedure(schoolID:int, leaderScore:int):
#     cursor = conn.cursor()
#     sql = f"UPDATE {public_schools_table_name} SET Leaders_Score = {leaderScore} WHERE School_ID = {schoolID};"
#     sql2 = f"IF {leaderScore}>0 AND {leaderScore} <20 \
#           THEN UPDATE CHICAGO_PUBLIC_SCHOOLS \
#           SET Leaders_Icon ='Very Weak' \
#           WHERE School_ID = {schoolID}; \
#           ELSEIF {leaderScore} < 40 \
#           THEN UPDATE {public_schools_table_name} \
#           SET Leaders_Icon ='Weak' \
#           WHERE School_ID = {schoolID}; \
#           ELSEIF {leaderScore} < 60 \
#           THEN UPDATE {public_schools_table_name} \
#           SET Leaders_Icon ='Average' \
#           WHERE School_ID = {schoolID}; \
#           ELSEIF {leaderScore} < 80 \
#           THEN UPDATE {public_schools_table_name} \
#           SET Leaders_Icon ='Strong' \
#           WHERE School_ID = {schoolID}; \
#           ELSEIF {leaderScore} < 100 \
#           THEN UPDATE {public_schools_table_name} \
#           SET Leaders_Icon ='Very Strong' \
#           WHERE School_ID = {schoolID}; \
#           END IF;"
#     res = cursor.execute(sql)
#     print(res.fetchone())
#     cursor.execute(sql2)
#
#
#
# update_leaders_score_procedure(610038, 64)