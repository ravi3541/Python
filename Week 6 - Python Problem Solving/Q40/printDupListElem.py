# write a program to print the duplicates number from the list . Print output in comma separated list
# [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,01, 12,88,7,6,2].

def printDuplicate(l1):
    dupList = []
    
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):

            if l1[i] == l1[j] and l1[i] not in dupList:
                dupList.append(l1[i])
    

    print("\nDup List : ",dupList)


l1 = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,0, 12,88,7,6,2]
print("Original List = ",l1)
printDuplicate(l1)