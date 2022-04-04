#return remainder form two nos.

from cupshelpers import Printer


n1 = int(input("Enter number 1 : "))
n2 = int(input("Eter number 2 : "))


#Approach 1

print("\n Approach 1 : Using Try Catch")

try:
    res = n1%n2
    print(f'Remainder of {n1} / {n2} = {res}  ')

except ZeroDivisionError as e:
    print(e,"  Divide By Zero Exception Occured")






#Approach 2 

print("\n Using Function")

def getRemainder(a,b):
    try:
        res=n1%n2
        return res
    

    except ZeroDivisionError as e:
        print("Trying to divide by Zero")


print(f'Remainder of {n1} / {n2} = ',getRemainder(n1,n2))




#Approach 3 

print("\n Approach 3 : Using in built function")

try:

    quot,rem=divmod(n1,n2)
    print(f'Remainder of {n1} / {n2} = {rem}')

except ZeroDivisionError as e:
        print("Trying to divide by Zero")





#Approach 4

print("\n Approach 4 : Using classes and objects")


class Remainder:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2


    def getRem(self):
        try:

            res = self.n1 % self.n2
            return res


        except:
            print("Divide by Zero Exception")


rem = Remainder(n1,n2)
res2 = rem.getRem()
print(f'Remainder of {n1} / {n2} = {res2} ')