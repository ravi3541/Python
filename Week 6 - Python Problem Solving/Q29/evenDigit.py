# Write a program, which will find all such numbers between 0 and n (both included) such that each
# digit of the number is an even number. The numbers obtained should be printed in a
# comma-separated sequence on a single line.
# N is take input from console

n = int(input("Enter n : "))

def getEven(num):
    while(num>0):
        r = num % 10
        #print("r = ",r)
        if r % 2 == 0:
            num //= 10
            #print("num = ",num)
        else:
            return False

    return True


def getNum(n):
    for i in range(n+1):
        if(getEven(i)):
            print(i,end=",")


getNum(n)


