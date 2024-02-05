"""
Exercise 57
Question:  Jason To Dictionary!


"""

# Answer
import json
from pprint import pprint

with open("Files/company1.json","r") as file:
    d = json.loads(file.read())

pprint(d)