# inspired by https://towardsdatascience.com/supercharging-ms-sql-server-with-python-e3335d11fa17

import pyodbc
from datetime import datetime

class Sql:
    def __init__(self, database, server="server_name"):

        # connection string
        self.con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")

        # initialise query attribute
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now().strftime("%d/%m/%Y"))


sql = Sql('database123')  # initialise the Sql object

cur = sql.cursor()

cur.execute("SELECT * FROM Table")

for row in cur.fetchall():
    print row[0]

sql.close()

