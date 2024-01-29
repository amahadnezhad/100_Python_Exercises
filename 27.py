"""
Exercise 27
Question: Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1,
          and end time t2.
          To test your solution,
 call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2, respectively,
 and you should get the expected output.

Expected output:
0.5

"""
def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a

print(acceleration(0,10,0,20))