# Write a program to perform all basic mathematical operations


class arithmeticOp:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def subtract(self):
        return self.n1 - self.n2

    def multiply(self):
        return self.n1 * self.n2

    def divide(self):
        return self.n1 / self.n2


num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

op1 =arithmeticOp(num1,num2)
print(f'{num1} + {num2}  = {op1.add()}')
print(f'{num1} - {num2}  = {op1.subtract()}')
print(f'{num1} * {num2}  = {op1.multiply()}')
print(f'{num1} / {num2}  = {op1.divide()}')