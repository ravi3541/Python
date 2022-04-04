# write a program which accepts a string from the console and print it in reverse order.

str1 = input("Enter a String : ")


#Approach 1 : Using reversed()
print("\nApproach 1 : Using reversed() ")

def rev(str1):
    str1 = "".join(reversed(str1))
    return str1


print("Reversed String : ",rev(str1))




#Approach 2 : Using slicing
print("\nApproach 2 : Using slicing")
def revSlice(str1):
    str1 = str1[::-1]
    return str1

print("Reversed String : ",revSlice(str1))





#Approach 3 : Using loop
print("\nApproach 3 : Using Loop")
def revLoop(str1):
    revstr = ""

    for i in str1:
        revstr = i + revstr
    
    return revstr

print("Reversed String : ",revLoop(str1))
