"""
Exercise 97
Question: Advanced File Writer

"""
# Answer
file = open("Files/user_data_save_close.txt", 'a+')

while True:
    line = input("Write a Value: ")
    if line.lower() == "save":
        file.close()
        file = open("Files/user_data_save_close.txt", 'a+')
    elif line.lower() == "close":
        file.close()
        break
    else:
        file.write(line + '\n')
