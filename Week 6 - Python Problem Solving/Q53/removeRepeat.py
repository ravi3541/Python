# Remove repetitive elements from the list, list length should be 25 include number, char etc

l1 = []

for i in range(25):
    elem = input(f'Enter element {i} : ')
    l1.append(elem)
print("Original List",l1)

l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)


l1 = l2  

print("After removing repeated elements ",l1)

    