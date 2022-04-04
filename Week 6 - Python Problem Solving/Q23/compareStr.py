# Compare Strings by Count of Characters
# Create a function that takes two strings as arguments and 
# return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

str1 = input("Enter String 1 : ")
str2 = input("Enter String 2 : ")


#Approach 1 : Using len function
print("\n Approach 1 : Using len function")

def compareStr1(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    print(f'Len1 = {len1} \t Len2 = {len2}')
    if len1 == len2:
        return True
    else:
        return False


if compareStr1(str1,str2):
    print("True: Strings are of equal length")
else:
    print("False : Strings are not of equal length")



#Approach 2 : Using Loop
print("\n Approach 2 : Using Loop")

def compareStr2(s1,s2):
    len1=0
    len2=0

    for i in s1:
        len1+=1

    for j in s2:
        len2+=1

    print(f'Len1 = {len1} \t Len2 = {len2}')
    if len1 == len2:
        return True
    else:
        return False


if compareStr2(str1,str2):
    print("True: Strings are of equal length")
else:
    print("False : Strings are not of equal length")