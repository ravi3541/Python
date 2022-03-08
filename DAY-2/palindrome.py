#Method 1 using for loop
def palindrome1(in_str):
    rev = ""
    for i in in_str:
        rev = i + rev

    if in_str == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")


#Method 2 using slicing
def palindrome2(in_str):
    if in_str == in_str[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")


in_str="malayalam"
print("Method 1")
palindrome1(in_str)

print("\nMethod 2")
palindrome2(in_str)
