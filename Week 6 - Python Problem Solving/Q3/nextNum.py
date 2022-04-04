#Return next no. from Integer Passed

n = int(input("Enter a positive number : "))


#Approach 1

print("\n Approach 1")
while (n<0):
    print("you Entered negative no. please enter positive no. ")
    n=int(input("Enter a positive number : "))


print(f'Next no. after {n} is {n+1}')


#Approach 2 Using function

print("\n Approach 2 : Using function")

def next(n):
    return n+1

print("Using next function ",next(n))   




#Approach 3
print("\n Approach 3 : Using Class and object")

class nextNo:
    def getNext(self,n):
        return n+1


obj = nextNo()
print("Next no. is ",obj.getNext(n))
