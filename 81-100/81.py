"""
Exercise 81
Question:   Username And Password Checker
"""
# Answer
while True:
    usr = input("Username: ")
    with open ("Files/users.txt") as file:
        users = file.readline()
        users = [i.strip('\n') for i in users]
    if usr in users:
        print("Username Exists!")
        continue
    else:
        print('Username Is Fine')


while True:
    notes = []
    psw = input("Enter Password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("Yoy Need At Least One Number!")
    if not any(i.isupper() for i in psw):
        notes.append("You Need At Least One Uppercase Letter!")
    if len(psw) < 5:
        notes.append("You Need At Least 5 Characters")
    if len(notes) == 0:
        print("Password Is Fine!")
