#Concatenating Two Integer Lists
#Create a function to concatenate two integer lists.

list1 = [72,42,65,4,18,62]
list2 = [75,35,2,5,34,23]


#Approach 1 : Using + operator

print("Approach 1 : Using + operator")

resList1 = list1 + list2
print(f'list after concatenation : {resList1} ')






#Approach 2 : Using List Comprehension
print("\n Approach 2 : Using List comprehension")

def conCatList2(list1,list2):
    resList3 = [value for ls in [list1,list2] for value in ls ]
    print(resList3)
    return resList3

resList4 = conCatList2(list1,list2)
print(f'list after concatenation : {resList4} ')






#Approach 3 : Using append function
print("\n Approach 3 : Using append function")

def conCatList(ls1,ls2):
    for i in ls2:
        ls1.append(i)
    
    return ls1

resList2 = conCatList(list1,list2)
print(f'list after concatenation : {resList2} ')
