"""
Exercise 42
Question: Print out in each line the sum of homologous items of the two sequences.

Expected output:
    5
    7
    9
"""
a = [1, 2, 3]
b = (4, 5, 6)

# Answer

for i, j in zip(a, b):
    print(i + j)