"""
Write a Python program that creates a dictionary whose keys are integers from 1 to n and values are their squares. 
Example for n = 7 the dictionary will be of the form: 
{1: 1, 2: 4, 3: 9, 4:16, 5:25, 6:36, 7:49}
"""

n = int (input ("Enter the value of n  "))

# creating empty dictionary
d = dict ()

# browsing through integers from 1 to n and adding key and values to dictionary
for i in range (1, n + 1):
     d [i] = i * i

print (d)