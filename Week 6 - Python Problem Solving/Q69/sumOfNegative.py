# Create a function that takes a string containing integers as well as other characters and return the sum of the negative integers only.
# Ex negative_sum("22 13%14&-11-22 13 12") => -11 + -22 = -33

import re


def sumNegative(str1):
    reg = "-\d+"
    pattern = re.compile(reg)
    match = re.findall(pattern, str1)
    sum = 0

    for elem in match:
        sum += int(elem)
    
    return sum



str1 = input("Enter String including negetive numbers : ")

sum = sumNegative(str1)
print(f'Sum of negetive numbers in above string = {sum}')
