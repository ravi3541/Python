# Create a function that takes a number and returns its length(use of the len() function is prohibited)


def lenOfNum(n):
    str1 = str(n)
    len = 0
    for i in str1:
        len += 1
    
    return len

num = input("Enter a number : ")
length = lenOfNum(num)
print(f'length of {num} = {length}')
