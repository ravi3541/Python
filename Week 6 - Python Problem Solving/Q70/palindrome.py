# Write a program to identify if number is palindrome or not 



num = int(input("Enter a number : "))
print(f'type of {num} = {type(num)}')

temp = num
rev = 0

while num != 0:
    
    r = num % 10
    rev = (rev * 10) + r
    num = num // 10
    

if rev == temp:
    print(f'Number is palindrome ')
else:
    print(f'Number is not a palindrome')