"""
Exercise 29
Question:  Please write a function that calculates liquid volume in a sphere using the following formula.
           The radius r is always 10,so consider making ita default parameter.


Expected output:
    4071.5040790523717
"""

# Answer

from math import pi

def volume(h, r=10):
    v = ((4 * pi * r**3) / 3) - (pi * h**2 * (3*r - h) / 3)
    return v

print(volume(2))