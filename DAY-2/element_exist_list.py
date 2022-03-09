#Check if element exist in list

import random as r

random_list = []
for i in range(20):
    random_list.append(r.randint(1,200))


print("Random List  ",random_list)
n=int(input("Input a no. to check if it exist in list  "))


print(f"Checking if {n} exists in list ( using loop ) : ")
for i in range(20):
    if(random_list[i] == n) :
        print (f"{n} Exists")
        break
else:
    print(f" {n} not Exists")



print(f"Checking if {n} exists in list ( using in ) : ")
if (n in random_list):
    print (f"{n} Exists")
else:
    print(f" {n} not Exists")