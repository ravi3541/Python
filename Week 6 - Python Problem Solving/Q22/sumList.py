# Get the Sum of All List Elements
# Create a function that takes a list and returns the sum of all numbers in the list.

list1 = [6,9,12,31,26,19]
print("list = ",list1)


#Approach 1 : Using For loop
print("\n Approach 1 : Using For loop")
def sumList1(ls):
    sum=0
    for i in ls:
        sum += i
    
    return sum


print(f'Sum of list elements = {sumList1(list1)} ')




# Approach 2 : Using sum function 

print("\n Approach 2 : Using sum function ")
def sumList2(ls):
    
    return sum(ls)


print(f'Sum of list elements = {sumList2(list1)} ')

