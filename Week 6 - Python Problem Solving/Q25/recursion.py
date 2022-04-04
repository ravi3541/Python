# Recursion to Repeat a String n Number of Times
# Create a recursive function that takes two parameters and repeats the string n number of times. 
# The first parameter text is the string to be repeated and the second parameter is the number of times the string is to be repeated.



def recur(s1,n):
    
    if n>0:
        
        recur(s1,n-1)
        print(s1)
        

        
        
recur("hi",5)