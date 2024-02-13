"""
Exercise 85
Question:  Please download the attached countries-raw.txt file. The file contains the list of country names,
           but it also contains some unnecessary text among the countries.
           Please clean the list with Python by generating a new text file that contains a flawless list of country
           names without any other text or brake lines in it.
           The new file content should look like in the expected output.

"""
# Answer
with open("Files/countries-raw.txt", 'r') as file:
    content = file.readlines()

content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i != ""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) != 1]

print(content)

with open("Files/countries-clean.txt", 'w') as file:
    for i in content:
        file.write(i+"\n")
