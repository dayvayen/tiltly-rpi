import sqlite3
from updateSQL import create_connection

n_records = raw_input("Number of records to show: ")
db_file = raw_input("Enter database name: ")
beerName = raw_input("Enter beer table name: ")



def getBeerRecords(db_file, beerName, n_records):
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + beerName + " ORDER BY time DESC LIMIT " + n_records)
    rows = cur.fetchall()
    for row in rows:
        print(row)

getBeerRecords(db_file, beerName, n_records)
