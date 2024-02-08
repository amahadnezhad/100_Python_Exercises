"""
Exercise 76
Question: Make a script that prints out the current day and time. For example Today is Sunday, December 25, 2016 .

"""
# Answer
from datetime import datetime

print(datetime.now().strftime("Today is %A, %B %d, %Y"))