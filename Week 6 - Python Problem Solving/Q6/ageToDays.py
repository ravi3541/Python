#Convert Age to Days

age = int(input("Enter your age : "))

#Approach1

print("\n Approach 1")
ageInDays = age * 365
print(f'You lived {ageInDays} days')


#Approach2
print("\n Approach 2 : Using Function")

def ageToDays(age):
    days = age * 365
    return days

days = ageToDays(age)
print(f'You lived {days} days ')



#Approach3
print("\n Approach 3 : Using Class")

class convertAge:
    def __init__(self,age):
        self.userAge = age


    def ageToDay(self):
        lived = self.userAge * 365
        return lived


obj = convertAge(age)
livedDays = obj.ageToDay()
print(f'You lived {livedDays} days ')        

