# Concatenate two list in following 
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]  output : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatList(l1,l2):
    l3 = []
    for i in l1:
        for j in l2:
            l3.append(i + j)
    
    print(l3)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]  
concatList(list1,list2)
