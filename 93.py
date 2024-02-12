"""
Exercise 93
Question:  Please Use the attached  file.  there's a directory named subdirs.
           That directory contains other directories inside.
           Please write a script that counts the number of .py files contained inside subdirs and all its sub-directories.

"""
# Answer
import glob

file_list = glob.glob("Files/subdirs/**/*.py", recursive=True)
print(len(file_list))