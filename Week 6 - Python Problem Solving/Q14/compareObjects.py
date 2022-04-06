#Check if objOne Is Equal to objTwo
#Create a function that checks to see if two object arguments are equal to one another. 
#Return True if the objects are equal, otherwise, return False.

import time

#Comparing List Objects
print("\ncomparing lists\n")

list1 = ["ravi","anant","rajat","vikas","suraj"]
list2 = ["ravi","anant","rajat","vikas","suraj"]

print(f'list 1 = {list1}')
print(f'list 2 = {list2}')

if list1 == list2:
    print("\n list1 and list2 are equal")
else:
    print("\n list1 and list2 are not equal")



#Comparing Class Objects
print("\n comparing objects")

class fruit:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class animal:
    def __init__(self,species,name):
        self.species = species
        self.name = name


fruit1 = fruit("mango", 200)
fruit2 = fruit("apple", 150)
fruit3 = fruit("mango", 200)
animal1 = animal("reptiles","lizard")


def compareObj(obj1,obj2,className):
    if( isinstance(obj1,className) and isinstance(obj2,className)):
        print("both objects belong to same class")

        print(" Comparing instance attributes.......")
        time.sleep(1)
        if( obj1.name == obj2.name and obj1.price == obj2.price ):
            print("Objects are equal")
        else:
            print("Objects are not equal beacuse one or more instance varible not matched")
    else:
        print("objects dont belong to same class")

    print("-------------------------------------------------------")


print(" fruit 1 = { name: ",fruit1.name,", price: ",fruit1.price," }")
print(" fruit 2 = { name: ",fruit2.name,", price: ",fruit2.price," }")
print(" fruit 3 = { name: ",fruit3.name,", price: ",fruit3.price," }")
print(" animal 1 = { species: ",animal1.species,", name: ",animal1.name," }")


print("\n comparing fruit 1 and fruit 2")
time.sleep(1)
compareObj(fruit1,fruit2,fruit)



print("\n comparing fruit 1 and fruit 3")
time.sleep(1)
compareObj(fruit1,fruit3,fruit)


print("\n comparing fruit 1 and  animal 1")
time.sleep(1)
compareObj(fruit1,animal1,fruit)