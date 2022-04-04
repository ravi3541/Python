# Divides Evenly
# Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.


a = int(input("Enter a : "))
b = int(input("Enter b : "))

def division(a,b):
    try:
        if a % b == 0:
            return True
        else:
            return False
    except ZeroDivisionError:
        print("Zero Division Error Occured")


if division(a,b):
    print(f'True : {a} is evenly divisible by {b}')
else:
    print(f'False : {a} is not divisible by {b}')
            