#Find factorial of n

n =int(input("Enter n to find its factorial : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of ",n," = ",fact)