#Print prime nos in range 0 to n

n= int(input ("Please, Enter n : "))  
print ("The Prime Numbers in the range 0 to ",n," are ")  
for number in range (0, n+1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)