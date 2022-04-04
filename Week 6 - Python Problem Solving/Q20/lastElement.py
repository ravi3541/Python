# Return the Last Element in a List
# Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.
 
list1 = ['Car',83,"Laptop",74.37,"Book"]

#Approach 1 : Using negative Index
print("\n Approach 1 : Using negative Index")

def lastElemList1(ls):
    return ls[-1]


print(" Last Element of list is : ",lastElemList1(list1))


#Approach 2 : Using for loop
print("\n Approach 2 : Using for loop")

def lastElemList2(ls):
    n = len(ls)
    for i in range(n):
        if i == n-1:
            return ls[i]


print(" Last Element of list is : ",lastElemList2(list1))

