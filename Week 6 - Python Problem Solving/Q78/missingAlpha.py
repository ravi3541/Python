# Given a string of letters in the English alphabet, return the letter that's missing from the string. The missing letter will make the string be in alphabetical order (from A to Z).
# If there are no missing letters in the string, return "No Missing Letter".
# missingLetter("abdefg") ➞ "c"


def getMissingCharList(s1):
    minimum = min(s1)
    maximum = max(s1)

    alpha = []
    for i in range(ord('a'),ord('z')+1):
        if chr(i) >= minimum and chr(i)<= maximum:
            alpha.append(chr(i))
    
    #print(f'Alpha = {alpha}')
        

    missing_char = []
    for ch in alpha:
        # for s in range(ord(minimum),ord(maximum)):
        if ch not in s1:
            missing_char.append(ch)

    print(f'Missing chars = {missing_char}')


input_Str = input("Enter a string without space : ")
input_Str = input_Str.replace(' ','').lower()
print(f'Input str = {input_Str}')

getMissingCharList(input_Str)

