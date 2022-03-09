#Write a recursive function to compute x^y

def power(N, P):

	# if power is 0 then return 1
	# if condition is true only then it will enter it , otherwise not
	if P == 0: # base condition
		return 1

	return (N*power(N, P-1)) # recursive call


N = int(input("Enter a no. "))
P = int(input("Enter its power  "))

print(power(N, P))
