"""
Exercise 36
Question:  Create a function that takes a text file as input and returns the number of words contained.

"""

text = "A tree is a woody perennial plant, typically with branches."

# Answer
def count_words(text):
        text = text.split(" ")
        return len(text)

print(count_words(text))