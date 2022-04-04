# Write a program to square each odd number in a list.
# Take a list - list contains at least 20 elements


print("Enter 20 numbers ")
l1 = []

for i in range(0,20):
    a = int(input(f'Enter no.{i+1} '))
    l1.append(a)    


def squareOddNum(l):
    squareList = []
    for i  in l:
        if int(i) % 2 != 0:
            squareList.append(int(i)**2)
        else:
            squareList.append(int(i))

    return squareList


print("l1  = ",l1)
l2 = squareOddNum(l1)
print("l2  = ",l2)