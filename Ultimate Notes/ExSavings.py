# Exercise 2 starts on line 40

class Account:
    def __init__(self, acctNumber, balance):
        self.acctNumber = acctNumber
        self.balance = balance
        
    def __str__(self):
        return 'Account number: ' + str(self.acctNumber) + '\n' + \
               'Balance: ' + str(self.balance)
               
        def deposit(self, amount):
            self.balance += amount

class Checking(Account):
    def __init__(self, acctNumber, balance, fee):
        Account.__init__(self, acctNumber, balance)
        self.fee = fee
    
    def __str__(self):
        retStr = 'Account type: Checking\n';
        retStr += Account.__str__(self)
        return retStr

    def getFee(self):
        return self.fee
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance = self.balance - amount - self.fee
            



# Exercise 2
class Savings(Account):
    def __init__(self, acctNumber, balance):
        Account.__init__(self, acctNumber, balance)
    
    def __str__(self):
        retStr = 'Account type: Savings\n'
        retStr += Account.__str__(self)
        return retStr
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance = self.balance - amount
            

ca = Checking('123', 500, .50)
print(ca)  # Account type: Checking
            # Account number: 123
            # Balance: 500
ca.withdraw(100)
print(ca)  # Account type: Checking
            # Account number: 123
            # Balance: 399.5
sa = Savings('456', 1000)
print(sa)  # Account type: Savings
            # Account number:  456
            # Balance: 1000
sa.withdraw(250)
print(sa)  # Account type: Savings
            # Account number: 456
            # Balance: 750
sa.deposit(125)
print(sa)  # Account type: Savings
            # Account number: 456
            # Balance: 875