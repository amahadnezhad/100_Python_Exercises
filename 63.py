"""
Exercise 63
Question: Create a program that, once executed the programs prints Hello  instantly first,
          then it prints it after 1 second, then after 2, 3,
          and then the program prints out the message "End of the Loop" and stops.

Expected output:
Hello
Hello
Hello
Hello
End of Loop

"""
# Answer
import time

i = 0
while True:
    print('hello')
    i = i + 1
    if i > 3:
        print("End of Loop")
        break
    time.sleep(i)
