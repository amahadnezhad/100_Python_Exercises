"""
Exercise 71
Question: Count the number of "a" characters in this text file:http://www.pythonhow.com/data/universe.txt

Expected output:
264
"""
import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
count_a = text.count("a")
print(count_a)