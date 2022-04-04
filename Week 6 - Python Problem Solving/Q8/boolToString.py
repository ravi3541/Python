#boolean to String Conversion

a = True
print(f'\nType of a = {type(a)} ')


#Approach 1
print("\n Approach 1 : Using Built in str() function")

print(f'After conversion Type of a = {type(str(a))} ')


#Approach 2
print("\n Approach 2 : Using : function")

def boolToStr(a):
    if(a):
        return "True"
    else:
        return "False"
    

str = boolToStr(a)
print(f'After conversion Type of a = {type(str)} ')

