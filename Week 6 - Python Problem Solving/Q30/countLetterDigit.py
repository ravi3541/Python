# Write a program that accepts a sentence and calculate the number of letters and digits and also
# calculates the upper and lower case letters


str1 = input("Enter a sentence : ")

def countLetterDigit(s1):
    countUpper = 0
    countLower = 0
    countDigit = 0
    countLetter = 0

    for s in s1:
        if s.isalpha():
            countLetter += 1
            if s.isupper():
                countUpper += 1
            elif s.islower():
                countLower += 1
        elif s.isdigit():
            countDigit += 1
    
    print(f' Letters = {countLetter} \n Uppercase  = {countUpper} \n Lowercase = {countLower} \n Digits = {countDigit} ')


countLetterDigit(str1)