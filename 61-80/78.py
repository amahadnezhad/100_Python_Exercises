"""
Exercise 78
Question: Create a program that generates a password of 6 random alphanumeric characters.

"""
# Answer
import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)
