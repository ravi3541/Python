#Program to check whether a no. is Armstrong or not
def power(no, p):
    if (int(p) == 0):
        return 1
    else:
        s = 1
        for i in range(1, p + 1):
            s = s * int(no)
        return s


def order(x):
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
    return n


x = int(input("Enter a no check if its armstrong or not : "))
n = int(order(x))
temp = x

sum = 0
while (temp != 0):
    rev = temp % 10
    sum = sum + power(rev, n)
    temp = temp // 10

if (sum == x):
    print(x, " is an Armstrong no.")
else:
    print(x, " is not an Armstrong no.")

