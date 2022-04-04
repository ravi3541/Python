#Find the Smallest Number in a List
#Create a function that takes a list of numbers and returns the smallest number in the list.


list1 = [23,42,2,7,43,33,52,94,27,44]
print("List = ",list1)


#Approach 1 : Using function
print("\nApproach 1 : Using Function")
def minList1(input):
    smallest = input[0]
    for i in input:
        if i < smallest:
            smallest = i
    
    return smallest


print("smallest element from list = ",minList1(list1))





#Approach 2 : Using min function
print("\nApproach 2 : Using min function")
def maxList2(input):
    return min(input)

print("smallest element from list = ",maxList2(list1))




#Approach 3 : By sorting list
print("\nApproach 3 : By sorting list ")
n = len(list1)

def sortList(input):
    for i in range(n-1):
        for j in range(i+1,n):
            if input[j]<input[i]:
                input[j],input[i] = input[i],input[j]


    return input[0]


print("smallest element from list = ",sortList(list1))
