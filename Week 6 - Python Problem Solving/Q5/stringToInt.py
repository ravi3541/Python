#Return a String as an Integer


str = input("Enter a no : ")
print(f'Type of "{str}" is  {type(str)}')



#Approach 1
newStr1=int(str)
print("\n Approach 1 \n After converting to INT ")
print(f'Type of "{str}" after conversion is {type(newStr1)} ')




#Approach 2

print("\n Approach 2 : Using function")
def strToInt(str):
    newStr2 = int(str)
    print(f'Type of {str} after conversion is {type(newStr2)} ')
    return newStr2

temp = strToInt(str)




#Approach 3 
print("\n Approach 3 : Using class")

class strInt:
    def __init__(self, str2):
        self.str2 = str2

    
    def convertInt(self):
        newStr3 = int(self.str2)
        return newStr3


obj = strInt(str)
print(f'Type of {str} after conversion is {type(obj.convertInt())} ')
    





