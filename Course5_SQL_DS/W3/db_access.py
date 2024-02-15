import os
import mysql.connector
from dotenv import load_dotenv

'''Create a mySQLConnection'''
class Connection:

    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = 'password'
        self.database = 'hr'
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database:", self.database)
        except Exception as e:
            print('Exception connecting to database', self.database, ': \n', e)

    def disconnect(self, debug=False):
        if self.connection.is_connected():
            self.connection.close()
            if debug:
                print("Disconnected from MySQL database.")

    def start_transaction(self, debug=False):
        self.connection.start_transaction()
        if debug:
            print("Transaction started.")

    def commit_transaction(self, debug=False):
        self.connection.commit()
        if debug:
            print("Transaction committed.")

    def rollback_transaction(self):
        self.connection.rollback()
        print("Transaction rolled back.")

    def execute_query(self, query, debug=False):
        try:
            if debug:
                print("Query Beginning Execution")
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            print("Query Completed.")
            print(result)
            return result
        except Exception as e:
            print(e)


    def getDatabaseName(self):
        return self.database

    def setDatabaseName(self, name):
        self.database = name

dbConn = Connection()
dbConn.connect()
dbConn.execute_query(query="SELECT * FROM employees;")