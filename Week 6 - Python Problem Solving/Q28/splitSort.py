# Write a program that accepts a comma separated sequence of words as input and 
# prints the words in a comma-separated sequence after sorting them alphabetically.


s1 = input("Enter comma seperated sequence if words : ")


def splitSort(s1):
    l1 = s1.split(",")
    a = sorted(l1)

    

    print("output : ")
    for i in a:
        print(i,end=",")



splitSort(s1)