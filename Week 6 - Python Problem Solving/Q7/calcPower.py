#Calculate power

num = int(input("Enter a number : "))
p = int(input("Enter its  power : "))


#Approach 1
print("\n Approach 1")
res = 1
for i in range(p):
    res = res * num


print(f' {num}^{p} = {res} ')



#Approach 2

print("\n Approach 2 : Using function")

def calPow(n,p):
    res2 = 1
    while(p>0):
        res2 = res2 * n
        p-=1

    return res2


print(f'{num}^{p} = {calPow(num,p)} ')         


#Approach 3 
print("\n Approach 3 : using built in function pow()")
print(f'{num}^{p} = {pow(num,p)} ')



#Approach 4
print("\n Approach 4 Using Class")

class calcPower:
    def __init__(self,num,p):
        self.num = num
        self.p = p

    
    def getPower(self):
        res3 = 1
        for i in range(self.p):
            res3 = res3 * self.num
        
        return res3


obj = calcPower(num,p)
print(f'{num}^{p} = {obj.getPower()} ')

