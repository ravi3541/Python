# Find the day of the week from given date , dae input from console


import datetime
import calendar

def dayOfWeek(date):
	day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
	return (calendar.day_name[day])



date = input("Enter date in dd mm yyyy format : ")
print(dayOfWeek(date))
