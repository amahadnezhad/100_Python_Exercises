"""
Exercise 35
Question: Create a function that takes any string as input and returns the number of words for that string.

"""

# Answer
def txt(text):
    text = text.split()
    return len(text)

text = "Hey How Are You"
print(txt(text))
