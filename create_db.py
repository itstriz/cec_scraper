import sqlite3 as lite
import sys

con = lite.connect('closings.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Closings(id INT, name TEXT, status TEXT, closed BOOL, date DATE)")

