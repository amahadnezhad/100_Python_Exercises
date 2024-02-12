"""
Exercise 89
Question:

"""
# Answer
import sqlite3

conn = sqlite3.connect('Files/database.db')
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

for i in rows:
    print(i[0])
