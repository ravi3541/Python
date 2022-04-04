# write a program to print the list after removing the 0th,4th,5th numbers from list
# List [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,01].



#Approach 1 : Using pop()


def popRemove():
    l1 = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
    print("List = ",l1)
    l1.pop(5)
    l1.pop(4)
    l1.pop(0)
    print("List after deleting 0th, 4th & 5th element = ",l1)


#Approach 2 : Using del


def delRemove():
    l1 = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
    print("List = ",l1)

    del l1[5]
    del l1[4]
    del l1[0]
    print("List after deleting 0th, 4th & 5th element = ",l1)



#Approach 3 : Using For loop


def listRemove():
    l1 = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
    print("List = ",l1)

    rmv = []
    
    for i in range(len(l1)):
        if i == 0 or i == 4 or i ==5:
            rmv.append(l1[i])

    for i in rmv:
        l1.remove(i)

    print("List after deleting 0th, 4th & 5th element = ",l1)


print("\nApproach 1 : Using pop()")
popRemove()

print("\nApproach 2 : Using del")
delRemove()

print("\nApproach 3 : Using for loop")
listRemove()



