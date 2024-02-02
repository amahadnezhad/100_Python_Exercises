"""
Exercise 43
Question: Question: Create a script that generates a list where all letters of the English alphabet are listed
                    three in each line.

Expected output:
    abc
    def
    ghi
    .
    .
    .
"""
# Answer
import string

letters = string.ascii_lowercase + " "

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]

output = []

for s1, s2, s3 in zip(slice1, slice2, slice3):
    output.append(s1 + s2 + s3)


for item in output:
    print(item)
