import pyodbc
drive = 'SQL Server'
sever = 'DUCKHEE\\SQLEXPRESS'
database = 'BikeStores'
username = 'ASUS'
password = ''
str_sql = 'DRIVER={0};SERVER={1};DATABASE={2};UID{3};PWD={4}'.format(drive, sever, database, username, password)

cnxn = pyodbc.connect(str_sql)
cursor = cnxn.cursor()

query = """SELECT first_name, last_name, email, phone
                 FROM sales.staffs"""
cursor.execute(query)
 # Cách 1 select
for row in cursor:
     print(row)

# Cách 2 select
# row = cursor.fetchone()
# while row:
#     print(row)
#     row = cursor.fetchone()

# Insert
# cursor.execute("in")

# import pyodbc
#
# print(pyodbc.drivers())
