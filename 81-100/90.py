"""
Exercise 90
Question: DataBase To Csv Converter

"""
# Answer
import sqlite3
import pandas

conn = sqlite3.connect("Files/database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

df = pandas.DataFrame.from_records(rows)
df.columns = ["Rank", "Country", "Area", "Population"]
df.to_csv("Files/countries_big_area.csv", index=False)
