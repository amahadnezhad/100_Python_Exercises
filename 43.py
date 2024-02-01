"""
Exercise 43
Question: Create a script that generates a List where all letters of the English alphabet are listed two in each line

Expected output:
    ab
    cd
    ef
    .
    .
    .
"""
# Answer

import string

alphabet = []

for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
    alphabet.append(letter1 + letter2)

for item in alphabet:
    print(item)