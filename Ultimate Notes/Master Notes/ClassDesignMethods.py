# Two string method  14
# 
# 
# 
# 
class Name:     # class Name is usually capitalized
    # constructor - instantiation   ****  a fancy way of saying we want to create an instance of a class. Each instance of a class is an object and those objects have to be created. A constructor is a function
    def __init__(self, first, middle, last):   # self refers to the current instance of a class, followed by the rest of the parameters that define the rest of the class.
        self.first = first
        self.middle = middle
        self.last = last
        
        
 # Two string method
#     def __str__(self):
#         return self.first + ' ' +  self.middle + ' ' + self.last

# aName = Name('Mary', 'Liz', 'Smith')
# print(aName)  # Mary Liz Smith
# print('aName is ' + str(aName))  # aName is Mary Liz Smith



 # Two string method

    def __str__(self):
        return self.first + ' ' +  self.middle + ' ' + self.last
    
    def lastFirst(self):
        return self.last + ' ' + self.first + ' ' + self.middle
    
    def initials(self):
        return self.first[0] + self.middle[0] + self.last[0]

aName = Name('Mary', 'Liz', 'Smith')
print(aName)  # Mary Liz Smith
print('aName is ' + str(aName))  # aName is Mary Liz Smith
print(aName.lastFirst())  # aName is Mary Liz Smith
print(aName.initials())  # MLS