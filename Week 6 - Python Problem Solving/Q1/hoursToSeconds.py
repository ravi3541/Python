# Python Program to convert Hours into seconds


from datetime import timedelta


hrs = int(input("Enter Hours : "))


# Approach 1

print("\n Approach 1")
sec = hrs * 3600
print(f'{hrs} hours = {sec} seconds')


# Approach 2 : Using Class
print("\n Approach 2 : Using Class")


class hrsToSec:
    def __init__(self, hours):
        self.hours = hours

    def dispHrsToSec(self):
        seconds = self.hours * 3600
        print(f'{self.hours} hours = {seconds} seconds')


obj = hrsToSec(hrs)
obj.dispHrsToSec()


# Approach 3 : Using Function
print("\n Approach 3 : Using Function")


def funcHrsToSec(hrs):
    print(f'{hrs} hours = {hrs*3600} seconds')


funcHrsToSec(hrs)


# Approach 4 : Using datetime module

print("\n Approach 4 : Using datetime module")

seconds = timedelta(hours=hrs).total_seconds()

print(f'{hrs} hours = {seconds} seconds')
