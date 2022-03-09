"""

    Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
    Create a constructor with parameters: accountNumber, name, balance.
    Create a Deposit() method which manages the deposit actions.
    Create a Withdrawal() method  which manages withdrawals actions.
    Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
    Create a display() method to display account details.
    Give the complete code for the  BankAccount class.

"""


class BankAccount:
     
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    
    def Deposit(self , d ):
        self.balance = self.balance + d
    
    
    def Withdrawal(self , w):
        if(self.balance < w):
            print("Insufficient balance !")
        else:
            self.balance = self.balance - w
    

    def bankFees(self):
        self.balance = (95/100)*self.balance
        
    

    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")
        


newAccount = BankAccount(2178514584, "Tejas" , 2700)

newAccount.bankFees()
newAccount.display()

newAccount.Withdrawal(300)

newAccount.Deposit(200)

print("\nafter withdrawl and deposit action\n")
newAccount.display()