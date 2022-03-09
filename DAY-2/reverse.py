#Reverse words in given string


def reverse(input): 
    words = input.split(' ') 
    rev_input = ' '.join(reversed(words)) 
    return rev_input 

input = 'Reverse the String'
print (reverse(input))