"""
Exercise 24
Question: Please complete the script so that it prints out the expected output.

Expected output:
    a Has Value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b Has Value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    c Has Value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


"""

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# Answer
for key, value in d.items():
    print(key, "Has Value", value)