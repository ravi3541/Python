# Create a function that takes an array of strings and returns an array with only the strings that have numbers in them. If there are no strings containing numbers, return an empty array.


import re


def getNumStrArr(l1):
    reg = "\d+"
    pattern = re.compile(reg)
    numArr = []

    for elem in l1:
        match = re.search(pattern, elem)
        if match:
            numArr.append(elem)
    
    return numArr



print("Enter 5 array elements : ")
strArr = []
for i in range(5):
    elem = input()
    strArr.append(elem)

print(f'Original Array : {strArr}')


numArr = getNumStrArr(strArr)
print(f'Array with elements that contains numbers : {numArr}')
