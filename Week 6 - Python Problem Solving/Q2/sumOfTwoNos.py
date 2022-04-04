#Sum of two Nos.


from re import A


n1 = int(input("Enter 1st no. : "))
n2 = int(input("Enter 2nd no. : "))

#Approach 1

print("\n Approach 1 ")
sum1 = n1+n2
print(f'{n1} + {n2} = {sum1}')



#Approach 2

print("\n Approach 2 : Using class")

class sumOfNos:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def returnSum(self):
        return self.a + self.b


obj = sumOfNos(n1,n2)
print(f'{n1} + {n2} = {obj.returnSum()}')



#Approach 3 
print("\n Approach 3 : Using Function")

def sumOfTwoNos(a,b):
    sum3 = a + b
    return (f'{a} + {b} = {sum3}')


print(sumOfTwoNos(n1,n2))

