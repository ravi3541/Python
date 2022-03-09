#Write a function to compute x^y using loop

def power(N, P):
    pow=1
    for i in range(P):
        pow=pow*N
	
    return pow


N = int(input("Enter a no. "))
P = int(input("Enter its power  "))

print(power(N, P))
