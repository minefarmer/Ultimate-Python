import math
# Global scope  10
# Local scope 13
# Local scope = Variable squared  17
# Local scope {lexical scope)} accessing Variable scope squared  22  ^^^ THIS IS NOT WORKING CODE == because it was accessed frim the global scope
# 
# Nested scope  35
# 
# 
# number = 1
# print(number)  # 1

# def getNumber():
#     print(number)
# getNumber()  # 1

# def square(number):
#     squared = number * number
#     return squared
# print(square(2))  # 4

# def square(number):
#     squared = number * number
#     return squared
# print('Squared (defined in square function): ' + str(squared))  # Traceback (most recent call last):
#                         # File "/home/carl/Github/Ultimate-Python/Ultimate Notes/Scope.py", line 26, in <module>
#                         #     print('Squared (defined in square function): ' + str(squared))
#                         # NameError: name 'squared' is not defined






# Lexical or Nested scope  ********************************************************
def hypotenuse(s1, s2):
    def square(num):
        return num * num
    return math.sqrt(square(s1) + square(s2))

print('Enter the length of side 1: ')  # 3
side1 = int(input())
print("Enter the length of side 2: ")  # 3
side2 = int(input())
hyp =hypotenuse(side1, side2)
print('The hypotenuse is ' + str(hyp))  # The hypotenuse is 5.0