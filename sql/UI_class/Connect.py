# Connect.py
import pyodbc

class KetNoi:
    def __init__(self, server, database, username='ASUS', password=None):
        if username and password:
            str_sql = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        else:
            str_sql = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"

        self.connection = pyodbc.connect(str_sql)
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        return self.cursor.execute(query)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
