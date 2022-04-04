# Find the Largest Number in a List
# Create a function that takes a list of numbers. Return the largest number in the list.

list1 = [23,42,2,7,43,33,52,94,27,44]
print("List = ",list1)


#Approach 1 : Using function
print("\nApproach 1 : Using Function")
def maxList1(input):
    largest = input[0]
    for i in input:
        if i > largest:
            largest = i
    
    return largest


print("largest element from list = ",maxList1(list1))





#Approach 2 : Using max function
print("\nApproach 2 : Using max function")
def maxList2(input):
    return max(input)

print("largest element from list = ",maxList2(list1))




#Approach 3 : By sorting list
print("\nApproach 3 : By sorting list ")
n = len(list1)

def sortList(input):
    for i in range(n-1):
        for j in range(i+1,n):
            if input[j]<input[i]:
                input[j],input[i] = input[i],input[j]


    return input[-1]


print("largest element from list = ",sortList(list1))
