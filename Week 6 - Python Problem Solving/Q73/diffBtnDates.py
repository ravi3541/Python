# Create a function that takes two dates and returns the number of days between the first and second date.

import  datetime as dt


def diffDate(dt1,dt2):
    
    diffDays = (dt2 - dt1).days
    return diffDays


try:
    start_date = input("Enter start date in YYYY MM DD format : ")
    end_date = input("Enter end date in YYYY MM DD format : ")

    start_date = dt.datetime.strptime(start_date, "%Y %m %d").date()
    end_date = dt.datetime.strptime(end_date, "%Y %m %d").date()

    if start_date > end_date:
        raise ValueError
    else:
        d = diffDate(start_date,end_date)
        print(f'Difference days = {d}')

except ValueError:
    print("Invalid Dates")
