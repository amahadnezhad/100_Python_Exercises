"""
Exercise 95
Question: Create a program that asks the user to input values separated by commas and stores those values in a text file
          , each value in a separate line.

"""
# Answer
line = input("Enter values: ")
line_list = line.split(",")
with open("Files/user_data_commas.txt", "a+") as file:
    for i in line_list:
        file.write(i + "\n")
