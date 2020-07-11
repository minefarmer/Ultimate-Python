# Tax  13
# Net pay   28
# 
# Factorial   50
# 
# 
# 0-240 0%
# 241-480 15%
# 481- 28%



# tax
# def tax(amount):
#     if amount <= 240:
#         return 0
#     elif amount > 240 and amount <= 480:
#         return amount * .15
#     else:
#         return amount * .28
    
# print('Enter amount: ')  # 300
# amount = int(input())
# print('The tax is ' + str(tax(amount)))  # 45



# Net pay
# def tax(amount):
#     if amount <= 240:
#         return 0
#     elif amount > 240 and amount <= 480:
#         return amount * .15
#     else:
#         return amount * .28
    
# def netpay(grosspay):
#     return grosspay - tax(grosspay)
    
# # print('Enter amount: ')  # 300
# # amount = int(input())
# # print('The tax is ' + str(tax(amount)))  # 45
# print('Enter gross pay: ')  # 1000
# gp = int(input())
# print('Net pay is ' + str(netpay(gp)))  # 720.0



#                  ***************************************************
def fact(number):
    product = 1
    for i in range(1,number+1):
        product *= i
    return product

print('Enter a number: ')  # 10
num = int(input())
print(str(num) + '! equals ' + str(fact(num)))  # 10! equals 3628800