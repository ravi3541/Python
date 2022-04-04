# Write a function to compute 5/0 and use try/except to catch the exceptions.

def exceptionDemo():
    try:
        n = 5//0
    except ZeroDivisionError:
        print("Exception Occured : Attempt to divide by zero")


exceptionDemo()
