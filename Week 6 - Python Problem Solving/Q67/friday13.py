# Given the month and year as numbers, return whether that month contains a Friday 13th

import datetime
import calendar


def dayOfWeek(date):
    try:
        day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        res = (calendar.day_name[day])
        #print("day  = ",res)
        if res == "Friday":
            return True
        else:
            return False

    except ValueError:
        print("Invalid Date")


date = "13 "
date += input("Enter  month and year in mm yyyy format : ")


if dayOfWeek(date):
    print("yes it contains 13th friday")
else:
    print("it does not contain 13th friday")




