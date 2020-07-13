# How we create an instance of a class  12
# 
class Name:     # class Name is usually capitalized
    # constructor - instantiation   ****  a fancy way of saying we want to create an instance of a class. Each instance of a class is an object and those objects have to be created. A constructor is a function
    def __init__(self, first, middle, last):   # self refers to the current instance of a class, followed by the rest of the parameters that define the rest of the class.
        self.first = first
        self.middle = middle
        self.last = last
        
        
        
# How we create an instance of a class
aName = Name('Mary', 'Liz' 'Smith')
yourName = Name('John','Larry','Brown')