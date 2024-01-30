"""
Exercise 31
Question:  Why do you get an error, and how would you fix it?

def foo(a=1, b=2):
    return a + b

x = foo - 1

"""

# Answer
def foo(a=1, b=2):
    return a + b

x = foo() - 1
print(x)