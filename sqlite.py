import pandas as pd
import sqlite3
con = sqlite3.connect(":memory:")  # make a database in memory or infile like 'example.db'

# make cursor object to call execute() method and run SQL commands:
cur = con.cursor()

# create table
cur.execute(
    '''
        CREATE TABLE friends (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    '''
)

# Insert  data
cur.execute("INSERT INTO friends VALUES (1,'Marcin','Nowak','777-888-999')")
cur.execute("INSERT INTO friends VALUES (2,'Daniel','Kowalski','777-888-111')")

# save changes
con.commit()



# run query with error handling
try:
    cur.execute("SELECT * from friends")
except sqlite3.Error as e:
    print("An error occurred:", e.args[0])

# print results method 1
# for row in cur:
#     print(row)

# print results method 2 - one record
# print(cur.fetchone())

# print results method 3 similar to method 1, but with save to variable
records = cur.fetchall()  # data as a list, inside tuples
for row in records:
    print(row)

# make a pandas dataframe
print(pd.DataFrame(records, columns=['id', 'name', 'surname', 'phone']))

# close connection
con.close()