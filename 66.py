"""
Exercise 66
Question: Write an English to Portuguese translation program.
          The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

"""
# Answer
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    return d[word]

word = input("Enter word: ")
print(vocabulary(word))