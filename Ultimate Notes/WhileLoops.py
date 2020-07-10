# Intro  11
# count controlled while loops  18
# Eventcontrolled loops  45
# Using continue  74
# Using break  112
# 
# 
# 
# 

# number = 1
# while number <= 10:
#     print(number)
#     number = number + 1
    
    

# count controlled while loops    *******************************
# sum = 0
# number = 1
# while number <= 10:
#     sum = sum + number
#     number = number = number + 1
# print('The sum is ' + str(sum))  # 55

# balance = 5000
# rate = 1.02
# year = 1
# while year <= 10:
#     balance = balance * rate
#     print('Year: ' + str(year) + ': ' + str(balance))  #  Year: 1: 5100.0
#                                                         # Year: 2: 5202.0
#                                                         # Year: 3: 5306.04
#                                                         # Year: 4: 5412.1608
#                                                         # Year: 5: 5520.4040159999995
#                                                         # Year: 6: 5630.81209632
#                                                         # Year: 7: 5743.4283382464
#                                                         # Year: 8: 5858.296905011328
#                                                         # Year: 9: 5975.462843111554
#                                                         # Year: 10: 6094.972099973786
#     year = year + 1
    
    
    
#  Eventcontrolled loops   ********************************************************
# average = 0.0
# total = 0
# count = 0
# print('Enter a grade (-1 to quit): ')
# grade = int(raw_input())
# while grade != -1:
#     total = total + grade
#     count = count + 1
#     print('Enter a grade (-1 to quit): ')
#     grade = int(raw_input())
# average = total / count
# print('Average grade: ' + str(average))
#             # Enter a grade (-1 to quit): 
#             # 100
#             # Enter a grade (-1 to quit): 
#             # 90
#             # Enter a grade (-1 to quit): 
#             # 80
#             # Enter a grade (-1 to quit): 
#             # 70
#             # Enter a grade (-1 to quit): 
#             # 60
#             # Enter a grade (-1 to quit): 
#             # -1
#             # Average grade: 80
            
            
            
# Using continue
# numer = 0
# denom = 0
# while denom != -1:
#     print('Enter a numerator: ')
#     numer = float(raw_input())
#     print('Enter a denominator: ')
#     denom = float(raw_input())
#     if denom == 0:
#         continue
#     print(numer / denom)
#                     # Enter a numerator: 
#                     # 4
#                     # Enter a denominator: 
#                     # 2
#                     # 2.0
#                     # Enter a numerator: 
#                     # 34
#                     # Enter a denominator: 
#                     # 13
#                     # 2.61538461538
#                     # Enter a numerator: 
#                     # 12
#                     # Enter a denominator: 
#                     # 0
#                     # Enter a numerator: 
#                     # 12
#                     # Enter a denominator: 
#                     # 4
#                     # 3.0
#                     # Enter a numerator: 
#                     # 12
#                     # Enter a denominator: 
#                     # -1
#                     # -12.0



# Using break
number = 0
total = 0
average =0.0
count = 0
while True:
    print('Enter a number: ')
    number = float(raw_input())
    if number ==  -1:
        break
    total = total + number
    count = count + 1
average = total / count
print('Average: ' + str(average))
