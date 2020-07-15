# How to write good code to prevent except errors NO 1  6
# How to write good code to prevent except errors NO 2  56
# 
# 
# 
# def calc(op1, op2, op):
#     if op == '+':
#         return op1 + op2
#     elif op == '-':
#         return op1 - op2
#     elif op == '*':
#         return op1 * op2
#     elif op == '/':
#         return op1 / op2
    
# cont = 'y'
# while cont != 'n':
#     print('Enter the first number: ')
#     num1 = int(input())
#     print('Enter the second number: ')
#     num2 = int(input())
#     print('Enter operation: ')
#     op = input()
#     if op == '/' and num2 == 0:
#         print('Cannot divid by zero.')
#         continue
#     else:
#         print(calc(num1, num2, op))
#     print('Do you want to continue(y/n'?)
#     cont = input()
#                         # Enter the first number: 
#                         # 3
#                         # Enter the second number: 
#                         # 2
#                         # Enter operation: 
#                         # *
#                         # 6
#                         # Enter the first number: 
#                         # 12
#                         # Enter the second number: 
#                         # 0
#                         # Enter operation: 
#                         # /
#                         # Cannot divid by zero.
#                         # Enter the first number: 
#                         # 12
#                         # Enter the second number: 
#                         # 3
#                         # Enter operation: 
#                         # /
#                         # 4.0
#                         # Enter the first number: 



# How to write good code to prevent except errors NO 2 
def calc(op1, op2, op):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2

import os

print('Enter file name to open ')
name = input()
while not os.path.isfile(name):
    print('File does not exist.')
    print('Enter file name to open: ')
    name = input()  # grades.txt
file = open(name, 'r')
for line in file:
    print(line,end='')  # 100
                        # 93
                        # 87
                        # 72
                        # 66
    
    
    
    
    

# cont = 'y'
# while cont != 'n':
#     print('Enter the first number: ')
#     num1 = int(input())
#     print('Enter the second number: ')
#     num2 = int(input())
#     print('Enter operation: ')
#     op = input()
#     if op == '/' and num2 == 0:
#         print('Cannot divid by zero.')
#         continue
#     else:
#         print(calc(num1, num2, op))
#     print('Do you want to continue(y/n'?)
#     cont = input()
