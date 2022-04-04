# Write a program which accepts a sequence of words separated by whitespace as input to print the
# words composed of digits only.
# Example : 2 cats and 3 dogs.
# Output should be :
# ['2', '3']
# [‘cats’, ‘dogs’]


def wordsDigits(list1):
    digits = []
    words =[]

    for s in list1:
        if s.isdigit():
            digits.append(s)
        else:
            words.append(s)
    
    print("Digits : ",digits)
    print("Words : ",words)


str1 = input("Enter a string composed of words and digits seperated by space : ")
l1 = str1.split()
wordsDigits(l1)


