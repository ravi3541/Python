# Write a function that returns the least common multiple (LCM) of two integers.


num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))
if(num1 > num2 ):   # Use If condition to find the greatest number among these two.
    max= num1
else:
    max= num2
while(True):
    if(max % num1 == 0 and max % num2 == 0):   
        print(f'LCM of {num1} and {num2} = {max}')
        break
    max= max+ 1