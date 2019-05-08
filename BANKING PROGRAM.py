import sys
class Customer:
    """Customer class with bank operation"""
    bankname=" Rockstar Bank "
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Available balance after deposit:",self.balance)
    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficient Balance : ")
            sys.exit()
        self.balance=self.balance-amt
        print("Balance amount after withdraw: ",self.balance)
print("Welcome to ", Customer.bankname)
name=input("Enter name of Customer\n  Your Name : ")
c=Customer(name)
while True:
    print('d-Deposit\nw-withdraw\n e-exit')
    option=input("Choose your option : ")
    if option=='d' or option=='D':
        amt=float(input('enter amount:'))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('enter amount:'))
        c.withdraw(amt)
    elif option == 'e' or option == 'E':
            sys.exit(0)
    else:
        print("invalid output\n please enter a valid output")
