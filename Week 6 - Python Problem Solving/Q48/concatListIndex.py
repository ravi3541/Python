# Concant two list index wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]


def concatList(l1,l2):
    l3 = []
    if len(l1) == len(l2):
        for i in range(len(l1)):
            l3.append(l1[i] + l2[i])

    else:
        print("Length of both lists should be same")

    return l3




n = int(input("Enter number of elements : "))
l1=[]
l2=[]

print("Enter elements for list 1")
for i in range(0,n):
    ele = input(f'Enter element {i} : ')
    l1.append(ele)


print("Enter elements for list 2")
for i in range(0,n):
    ele = input(f'Enter element {i} : ')
    l2.append(ele)


l3 = concatList(l1,l2)
print("\n Concatenated  list : ",l3)