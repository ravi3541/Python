#Convert Hours and Minutes into Seconds

from datetime import timedelta


hrs = int(input("Enter Hours : "))
mins = int(input("Enter minutes : "))



#Approach 1 : Using Function
print("\n Approach 1 : Using Methods")
def convertHrsMinToSec(h,m):
    hrsToSec = h * 3600
    minToSec = m * 60
    return hrsToSec+minToSec


print(f' {hrs} hrs and {mins} mins = {convertHrsMinToSec(hrs,mins)}  seconds')


#Approach 2 : Using timedelta
print("\n Approach 2 : using timedelta")
totalSeconds = timedelta(hours=hrs,minutes=mins).total_seconds()
print(f' {hrs} hrs and {mins} mins = {totalSeconds}  seconds')