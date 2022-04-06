# Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.

#returns hexadecimal for ascii value
def asciiToHex(val):
    char = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    rem = 1

    hex = []

    while rem != 0:
        rem = val % 16
        if rem > 9 and rem < 15:
            rem = char[rem]

        hex.append(rem)

        val = val // 16

    if hex[-1] == 0:
        hex.pop(-1)

    hex.reverse()

    str1 = ""
    for x in hex:
        str1 += str(x)
    #print("ascii to hex 1: ",str1)

    return str1

#Convert string to ascii and call asciiToHex()
def strToAscii(str):
    hex = ""
    for i in str:
        ch = ord(i)
        hex += asciiToHex(ch)

    print(f'\n {str} to hexadecimal = {hex}')

#Getting input from console
inStr = input("Enter a string to convert it to hexadecimal : ")
strToAscii(inStr)
