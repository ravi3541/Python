string = input("Enter string: ")
i = int(input("Enter position to be removed: "))
str1=string[:i]
str2=string[i+1:]
print(str1+str2)