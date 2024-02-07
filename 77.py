"""
Exercise 77
Question: Create a script that asks the user to enter their age,
          and the script calculates the user's year of birth and prints it out in a string like in the expected output.
          Please make sure you generate the current year dynamically.

"""
# Answer
from datetime import datetime

age = int(input("What's your age? "))
year_birth = datetime.now().year - age
print(f"We think you were born back in {year_birth}")