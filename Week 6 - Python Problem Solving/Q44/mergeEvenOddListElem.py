# Create a list by picking an odd-index items from the first list and even index items from the
# second
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# Output
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]
# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]

def mergeLists(l1,l2):
    len1 = len(l1)
    len2 = len(l2)

    oddL1 = []
    evenL2 = []

    for i in range(len1):
        if i % 2 != 0:
            oddL1.append(l1[i])
    
    for i in range(len2):
        if i % 2 == 0:
            evenL2.append(l2[i])

    print("\n Element at odd-index positions from list one : ",oddL1)
    print("\n Element at even-index positions from list two : ",evenL2)
    
    mergedList = oddL1 + evenL2

    print("Final Merged List : ",mergedList)

    return mergedList



l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

mergeLists(l1,l2)