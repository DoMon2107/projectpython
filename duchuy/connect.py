# ketnoi.py
import pyodbc

class Connect:
    def __init__(self, server, database, username=None, password=None):
        if username and password:
            str_sql = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        else:
            str_sql = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"

        self.connection = pyodbc.connect(str_sql)
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        return self.cursor.execute(query)

    def execute(self, query):
        self.cursor.execute(query)
        self.cursor.commit()

    def insert_(self, sql, params=None):
        try:
            if params is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, params)
            self.connection.commit()
            print("Insert thành công.")
        except Exception as e:
            print(f"Lỗi khi thực hiện insert: {e}")
            self.connection.rollback()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
