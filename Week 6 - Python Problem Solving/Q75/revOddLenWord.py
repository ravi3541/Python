# Given a string, reverse all the words which have odd length. The even length words are not changed.

def revOddLenWord(str1):
    split_str = str1.split()
    rev_string = " "

    for i in range(len(split_str)):

        if len(split_str[i]) % 2 != 0:
            rev = split_str[i][::-1]
            split_str[i] = rev
     
    rev_string = rev_string.join(split_str)
    return rev_string


input_str = input("Enter a string : ")
result = revOddLenWord(input_str)
print("Resultant String : ", result)
