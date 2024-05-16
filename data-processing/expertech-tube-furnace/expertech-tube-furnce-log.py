import csv, pyodbc

# set up some constants
MDB = 'C:/Users/alex.letwin/Desktop/Tool01 - 20240324_000005.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'
PWD = 'pw'

# connect to db
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb)};'
    r'SERVER=C:/Users/alex.letwin/Desktop/Tool01 - 20240324_000005.mdb;'
    # r'DATABASE=myDb;'
    r'Trusted_Connection=yes;'
)
con = pyodbc.connect(conn_str)
cur = con.cursor()

# run a query and get the results 
SQL = 'SELECT * FROM mytable;' # your query goes here
rows = cur.execute(SQL).fetchall()
print(rows)
cur.close()
con.close()