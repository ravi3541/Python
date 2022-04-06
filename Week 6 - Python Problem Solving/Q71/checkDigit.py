# Check char is digit without using isdigit() , take input from console 

def checkDigit(n):
    try:
        num = int(n)
        print("You entered a number")

    except ValueError:
        print("Invalid Input: you entered string")




digit = input("Enter a number : ")

checkDigit(digit)