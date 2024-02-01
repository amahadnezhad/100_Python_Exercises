"""
Exercise 25
Question: Make a script that prints out letters of the English alphabet from a to z, one letter per line in the terminal.

Expected output:
a
b
c
.
.
z
"""
# Answer
import string

for letter in string.ascii_lowercase:
    print(letter)