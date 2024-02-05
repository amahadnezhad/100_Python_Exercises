"""
Exercise 41
Question: Create a script that generates a List with all letters of the English alphabet inside it.

"""

# Answer
import string
letters = []

for letter in string.ascii_lowercase:
    letters.append(letter)

print(letters)