"""
Exercise 28
Question:  Why is there an error in the code, and how would you fix it?

"""
def foo(a, b):
    print(a + b)

# x = foo(2, 3) * 10
# print(acceleration(0,10,0,20)) # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

# Answer
def foo(a, b):
    return(a + b)

x = foo(2, 3) * 10
print(x)