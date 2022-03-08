"""
Write a function in Python that takes a list of integers as a parameter and returns a dictionary 
whose keys are the list integers and whose values are "even" or "odd" depending on the number. 
"""

def listToDict(l):
    
    #empty dictionary 
    evenOddDict = dict()
    
    # iterate over the list elements and test their parity
    for x in l:
        if x%2 == 0:
            evenOddDict[x] = 'Even'
        else:
            evenOddDict[x] = 'Odd'
    
    return evenOddDict



l = [24 , 14 , 3 , 36 , 41 , 22 , 15]
print(listToDict(l))