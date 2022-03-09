#Find max of 3 nos.

a=int(input("enter no. 1 : "))
b=int(input("enter no. 2 : "))
c=int(input("enter no. 3 : "))

if(a>b and a>c):
    print("a  = ",a," is max")
elif(b>a and b>c):
    print("b  = ",b," is max")
else:
    print("c  = ",c," is max")

