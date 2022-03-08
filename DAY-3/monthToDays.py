#Write a Python program to convert month name to a number of days.

month30=("april", "june", "september", "november")
month31=("january", "march", "may", "july", "august", "october", "december")

mon=input("Enter name of month to print days in that month  :  ")
mon=mon.lower()


if mon=="february":
    print(f"days in {mon} : 28")
elif mon in month30:
    print(f"days in {mon} : 30")
elif mon in month31:
    print(f"days in {mon} : 31")
else:
    print("You entered wrong input")


