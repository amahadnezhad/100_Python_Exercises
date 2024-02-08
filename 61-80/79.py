"""
Exercise 79
Question: Create a program that asks the user to enter a new password and check that the submitted password should
          contain at least one number, one uppercase letter, and at least 5 characters. If the conditions are generated,
          print out "Password is fine"; otherwise, keep prompting the user for a password.

"""
# Answer
while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")