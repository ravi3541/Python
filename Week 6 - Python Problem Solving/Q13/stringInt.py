#String to Integer and Vice Versa

str1 = input("Enter a number : ")
print(f' type of str1 is {type(str1)}')

print("\n converting str1 to integer..........")

try:
    str1 = int(str1)
    print(f'After converting string to int. Type of str1 is {type(str1)}')
except:
    print("\n Error occired while converting type")



print("\n converting str1 from int to string..........")
try:
    str1 = str(str1)
    print(f'After converting int to String. Type of str1 is {type(str1)}')
except:
    print("\n Error occired while converting type")

