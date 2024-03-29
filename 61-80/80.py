"""
Exercise 80
Question:   Create a program that asks the user to enter a new password and check that the submitted password should
            contain at least one number, one uppercase letter, and at least 5 characters. If the conditions are met,
            print out the reason why pointing to the specific condition/s that has not been satisfied.

"""
# Answer
while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)
