# The Farm Problem
# In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs
# The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.


ch_legs = 2
cow_legs = 4
pig_legs = 4

#Getting subtotal for animals
print("Enter Subtotal of all animals ")
ch = int(input("enter no. of Chickens : "))
cow = int(input("Enter no. of Cows : "))
pig = int(input("Enter no. of pigs : "))


#Approach 1
print("\n Approach 1 : Using function ")
def calcLegs(chickens,cows,pigs):
    total = (ch_legs * chickens) + (cow_legs * cows) + (pig_legs * pigs)
    return total


total_legs1=calcLegs(ch,cow,pig)
print("\n total legs = ",total_legs1)




#Approach 2 : Using Class
print("\n Approach 2 : Using class")
class animals:
    def __init__(self,chickens,cows,pigs):
        #initializing no. of chickens, cows and pigs
        self.chickens = chickens
        self.cows  = cows
        self.pigs  = pigs

    
    def calTotLegs(self):
        total = (self.chickens * ch_legs) + (self.cows * cow_legs) + (self.pigs * pig_legs)
        return total


animalObj = animals(ch, cow, pig)
total_legs2  = animalObj.calTotLegs()
print("\n Total Legs = ",total_legs2)
        


