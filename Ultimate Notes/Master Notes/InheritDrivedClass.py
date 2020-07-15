class Employee:
    def __init__(self, name, payRate):
        self.name = name
        self.payRate = payRate
        
    def __str__(self):
        return self.name + ', ' + str(self.payRate)
    
    def pay(self, hoursWorked):
        return self.payRate * hoursWorked

class Manager(Employee):
    def __init__(self, name, payRate, isSalaried):
        Employee.__init__(self, name, payRate)
        self.salaried = isSalaried
    
    def __str_(self):
        retStr = Employee.__str__(self)
        retStr += ' isSalaried: ' + str(self.isSalaried)
        return retStr
    
    def pay(self, hoursWorked):
        if self.salaried:
            return self.payRate
        else:
            return self.payRate * hoursWorked
    
el = Employee('John Jones', 10.00)
print(el)  # John Jones, 10.0
print('Gross pay: ' + str(el.pay(40)))  # Gross pay: 400.0
m1 = Manager('Jane Smith', 1200, True)
print(m1)  # Jane Smith, 1200
print('Gross pay: ' + str(m1.pay(40)))  # Gross pay: 1200
m2 = Manager('Jim Brown', 20.00, False)
print(m2)  # Jim Brown, 20.0
print('Gross pay: ' + str(m2.pay(40)))  # Gross pay: 800.0

