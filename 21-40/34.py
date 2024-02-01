"""
Exercise 34
Question:    The following script throws a NameError  in the last line saying that c  is not defined.
             Please fix the function so that there is no error and the  last line can print out the value of c .

def foo():
    c = 1
    return c
foo()
print(c)

Expected output:    1

"""

# Answer
def foo():
    global c # *
    c = 1
    return c
foo()
print(c)