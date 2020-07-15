# ZeroDivisionError: division by zero   18
# try to open a file that doesn't exist   32
# try - except ***  Cannot divide by zero.   41
# Opening a file that doesn't exist   63
# File type errors ie: IOERRORS   88
# Try - except ** Finally   114
# Creating our own exceptions  134
# 
# 
# 
# print('Enter a numerator: ')  # Enter a numerator:
# numer = int(input())  # 12
# print('Enter a denominator: ')  # Enter a denominator: 
# denom = int(input())  # 2
# quotient = numer / denom
# print(quotient)  # 6.0

# #  second run  **** ZeroDivisionError: division by zero
# print('Enter a numerator: ')  # Enter a numerator:
# numer = int(input())  # 12
# print('Enter a denominator: ')  # Enter a denominator: 
# denom = int(input())  # 0
# quotient = numer / denom
# print(quotient)  # 0
#                 # Traceback (most recent call last):
#                 # File "/home/carl/Github/Ultimate-Python/Ultimate Notes/Master Notes/ExceptionsHandling.py", line 23, in <module>
#                 #     quotient = numer / denom
#                 # ZeroDivisionError: division by zero



# try to open a file that doesn't exist    ******************************
# file = open('blah.txt', 'r')  # Traceback (most recent call last):
#                             # File "/home/carl/Github/Ultimate-Python/Ultimate Notes/Master Notes/ExceptionsHandling.py", line 33, in <module>
#                             #     file = open('blah.txt', 'r')
#                             # FileNotFoundError: [Errno 2] No such file or directory: 'blah.txt'




# #  try - except    ********   Cannot divide by zero.      *************************
# # try:
# #     code to be ExecutionLoader
# # except:
# #     code to run to handle the exceptions

# try:
#     print('Enter a numerator: ')  # Enter a numerator: 
#     numer = int(input())  # 12
#     print('Enter a denominator: ')  # Enter a denominator: 
#     denom = int(input())  # 0
#     quotient = numer / denom
#     print(quotient)
# except:
#     print('Cannot divide by zero.')  # Cannot divide by zero.
#     print('Enter a new denominator ')  # Enter a new denominator
#     denom = int(input())  $ 2
#     quotient = numer / denom
#     print(quotient)  # 6.0



# # Opening a file that doesn't exist
# try:
#     print('Enter the name of the file: ')
#     name = input()
#     file = open(name, 'r')

#     # print('Enter a numerator: ')  # Enter a numerator: 
#     # numer = int(input())  # 12
#     # print('Enter a denominator: ')  # Enter a denominator: 
#     # denom = int(input())  # 0
#     # quotient = numer / denom
#     # print(quotient)
# except:
#     print('Cannot open file.')
#     print('Enter the name of the file to open: ')
#     name = input()
#     file = open(name, 'r')
#     # print('Cannot divide by zero.')  # Cannot divide by zero.
#     # print('Enter a new denominator ')  # Enter a new denominator
#     # denom = int(input())  $ 2
#     # quotient = numer / denom
#     # print(quotient)  # 6.0



# # File type errors ie: IOERRORS   **************************
# try:
#     print('Enter the name of the file: ')
#     name = input()
#     file = open(name, 'r')

#     # print('Enter a numerator: ')  # Enter a numerator: 
#     # numer = int(input())  # 12
#     # print('Enter a denominator: ')  # Enter a denominator: 
#     # denom = int(input())  # 0
#     # quotient = numer / denom
#     # print(quotient)
# except IOError:
#     print('Cannot open file.')
#     print('Enter the name of the file to open: ')
#     name = input()
#     file = open(name, 'r')
# except ZeroDivisionError:
#     # print('Cannot divide by zero.')  # Cannot divide by zero.
#     # print('Enter a new denominator ')  # Enter a new denominator
#     # denom = int(input())  $ 2
#     # quotient = numer / denom
#     # print(quotient)  # 6.0



# # Try - except ** Finally   **************************
# # try:
# #     set of statements
# # except:
# #     set of statements
# try:
#     print('Enter the name of the file: ')
#     name = input()
#     file = open(name, 'w')
# except:
#     print('error with file.')
#     print('Enter the name of the file to open: ')
#     name = input()
#     file = open(name, 'w')

# finally:
#     file.close()
    
    
    
# Creating our own exceptions
class Rational:
    def __init__(self, x, y):
        numer = x
        if y == 0:
            raise ZeroDivisionError()
        else:
            denom = y

try:
    rat1 = Rational(4,1)
    rat2 = Rational(3,0)  # Traceback (most recent call last):
                    # File "/home/carl/Github/Ultimate-Python/Ultimate Notes/Master Notes/ExceptionsHandling.py", line 144, in <module>
                    #     rat2 = Rational(3,0)
                    # File "/home/carl/Github/Ultimate-Python/Ultimate Notes/Master Notes/ExceptionsHandling.py", line 139, in __init__
                    #     raise ZeroDivisionError()
                    # ZeroDivisionError
except:
    print('Cannot have a rational number with 0 for denominator,')  # Cannot have a rational number with 0 for denominator,