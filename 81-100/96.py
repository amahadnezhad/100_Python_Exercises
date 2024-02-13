"""
Exercise 96
Question: File Writer

"""
# Answer
file = open("Files/user_data.txt", 'a+')

while True:
    line = input("Write a Value: ")
    if line.lower() == "close":
        file.close()
        break
    else:
        file.write(line + "\n")

