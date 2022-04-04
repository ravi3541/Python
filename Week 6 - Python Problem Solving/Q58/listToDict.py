# Convert list into dictionary and add new item into dictionary

from os import sep


def listToDict(l1):
    dict1 = {}
    for i in range(0,len(l1),2):
        dict1[l1[i]] = l1[i+1]
    

    dict1['Tejas'] = 280 
    print("Dictonary : ",dict1.items())


list1 = ['ramesh',200,'manoj',220,'rajat',250,'vikas',260,'ravi',250]
listToDict(list1)