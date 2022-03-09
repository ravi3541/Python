#Write a program to accept n and print zig-zag pattern


n = int(input("Enter n to print zig zag pattern  "))
print("\n")

for row in range(1,4):

    for col in range(1,n+1):

        if (((row+col)%4==0) or (row==2 and col%4==0)):
            print("*",end="")
        else:
            print(" ",end="")
            
    print()
