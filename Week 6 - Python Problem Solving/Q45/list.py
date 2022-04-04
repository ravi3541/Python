# Remove items from list
# list1 = [54, 44, 27, 79, 91, 41]
# Out
# List After removing element at index 4 [34, 54, 67, 89, 43, 94]List after Adding element at index 2 [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last [34, 54, 11, 67, 89, 43, 94, 11]

list1 = [54, 44, 27, 79, 91, 41]
print("List 1 = ",list1)

list1.remove(91)
print("\nremoving 91 from list1 = ",list1)

list1.insert(2,50)
print("\ninserting 50 at index 2 = ",list1)

list1.pop(-1)
print("\nremoving last element = ",list1)

list1.append(100)
print("\ninserting 100 at last = ",list1)
