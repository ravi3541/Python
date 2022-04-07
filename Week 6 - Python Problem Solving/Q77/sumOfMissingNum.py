# Create a function that returns the sum of missing numbers.
# sumMissingNumbers([1, 3, 5, 7, 10]) ➞ 29
# // 2 + 4 + 6 + 8 + 9

def sumOfMissNum(l1):
    minimum = min(l1)
    maximum = max(l1)
    sum = 0
    for i in range(minimum,maximum):
        if i not in l1:
            sum += i

    return sum



try:

    num = []
    print("Enter list of 10 numbers")

    for i in range(5):
        elem = int(input())
        num.append(elem)
    
    sum = sumOfMissNum(num)
    print(f'Sum of missing numbers from list = {sum}')

except ValueError:
    print("Invalid Input, Only numbers allowed")
