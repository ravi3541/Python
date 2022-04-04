# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 7
# 6. No space accepted7. Maximum length of transaction password: 12 Your program should accept a sequence of
# comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma. Example
# If the following passwords are given as input to the program: ABd1234@1, Then, the
# output of the program should be: ABd1234@1


import re


def validatePass(paswd):
    reg = "(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])[a-zA-Z0-9@#$]{7,12}"
    pattern = re.compile(reg)

    match = re.search(pattern, paswd)

    if match:
        print(paswd,end=",")





passwords = input("Enter password sepearted by comma : ")
passList = passwords.split(",")

for value in passList:
    validatePass(value)


