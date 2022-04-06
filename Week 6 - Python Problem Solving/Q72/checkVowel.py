# Check if given char is vowel or consonant



def checkVowel(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U': 
        print("You entered a vowel")
    else:
        print("You Entered a consonant")


while True:
    char = input("Enter only one character : ")
    if len(char) == 1:
        checkVowel(char)
        break