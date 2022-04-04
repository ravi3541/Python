# Check if an Integer is Divisible By Five
# Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.


def divisible5(n):
    if n % 5 == 0:
        return True
    else:
        return False



num = int(input("Enter any number to check if it is divisible by 5 : "))
print(divisible5(num))