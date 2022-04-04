# Write a program that computes the net amount of a bank account based on a transaction log from
# console input.
# Log format is : D 100 W 200
# D means deposit while W means withdrawal. Suppose the following input is supplied to the
# program: D 300 D 300 W 200 D 100 Then, the output should be: 500

class transaction(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg



class account:
    def __init__(self):
        self.bal = 0

    def deposit(self,amt):
        self.bal += amt

    def withdrawl(self,amt):
        try:
            
            if self.bal > amt:
                self.bal -= amt
            else:
                raise transaction("Insufficient Balance")
        except transaction as t:
            print(t.msg)



log = input("Enter Transaction log : ")
transact = log.split(" ")
cust1 = account()

for i in range(len(transact)):
    if transact[i] == 'D':
        amt = int(transact[i+1])
        cust1.deposit(amt)
    elif transact[i] == 'W':
        amt = int(transact[i+1])
        cust1.withdrawl(amt)

    
print("Balance = Rs ",cust1.bal)