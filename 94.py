"""
Exercise 94
Question: Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash,
          so the content looks like in the expected output.

"""
# Answer
with open("Files/urls.txt", 'r') as file:
    lines = file.readlines()

print(lines)

with open("Files/urls_corrected.txt", 'w') as file:
    for line in lines:
        line_remove_s = line.replace('s', "", 1)
        line_remove_s_add_slash = line_remove_s[:6] + '/' + line_remove_s[6:]
        file.write(line_remove_s_add_slash)