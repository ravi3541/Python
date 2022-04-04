# Return first element of the list

fruits = ['mango', 'orange', 'apple', 'grapes', 'pineapple', 'guava']

print(f'Fruits list : {fruits} ')

# Approach 1
print("\n Approach 1 ")
print("Using positve indexing fruits[0] ", fruits[0])
print("Using negative indexing fruits[0] ", fruits[-len(fruits)])


# Approach 2

print("\n Approach 2 : using function")


def firstElemList(f):
    for pos in range(len(f)):
        if pos == 0:
            return f[pos]


firstFruit = firstElemList(fruits)
print("First Fruits = ", firstFruit)
