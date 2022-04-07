# Calculate the date 7 month from any date, take date input from console

import  datetime as dt
from dateutil.relativedelta import relativedelta



try:
    start_date = input("Enter start date in DD MM YYYY format : ")

    start_date = dt.datetime.strptime(start_date, "%d %m %Y").date()
    
    future_date = start_date + relativedelta(months = 7)
    f_date = future_date.strftime("%d %m %Y")
    print(f'\nDate after 7 months : {f_date}')
    

except ValueError:
    print("Invalid Date")
