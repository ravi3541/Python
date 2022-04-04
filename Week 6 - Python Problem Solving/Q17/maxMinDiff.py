#Difference of Max and Min Numbers in List
#Create a function that takes a list and returns the difference between the biggest and smallest numbers.


list1 = [23,42,2,7,43,33,52,94,27,44]
print("List = ",list1)


#Approach 1 : Using function
print("\nApproach 1 : Using Function")
def maxMinDiff(input):
    smallest = input[0]
    largest = input[0]
    for i in input:
        if i < smallest:
            smallest = i
        
        if i > largest:
            largest = i

    
    return largest - smallest


print("max min difference from list = ",maxMinDiff(list1))





#Approach 2 : Using max min function
print("\nApproach 2 : Using max min function")
def maxMin(input):
    return max(input) - min(input)

print("max min difference from list = ",maxMin(list1))




#Approach 3 : By sorting list
print("\nApproach 3 : By sorting list ")
n = len(list1)

def diffmaxMin(input):
    for i in range(n-1):
        for j in range(i+1,n):
            if input[j]<input[i]:
                input[j],input[i] = input[i],input[j]


    return input[-1] - input[0]


print("max min difference from list = ",diffmaxMin(list1))
