"""
Exercise 92
Question:  write a script that counts and prints out the number of .py files in that folder.

"""
# Answer
import glob

file_list = glob.glob1("Files/files", "*.py")
print(len(file_list))
