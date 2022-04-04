# Define a function that can accept two strings as input and print the string with maximum length in
# the console. If two strings have the same length, then the function should print all strings line by
# line.



def largeString(s1,s2):
    len1 = len(s1)
    len2 = len(s2)

    if len1 > len2:
        print(s1)
    elif len2 > len1:
        print(s2)
    elif len1 == len2:
        print(s1)
        print(s2)


str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")

largeString(str1,str2)