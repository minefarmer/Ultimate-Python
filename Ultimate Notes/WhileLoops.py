# Intro  11
# count controlled while loops  18
# 
# 
# 
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

balance = 5000
rate = 1.02
year = 1
while year <= 10:
    balance = balance * rate
    print('Year: ' + str(year) + ': ' + str(balance))  #  Year: 1: 5100.0
                                                        # Year: 2: 5202.0
                                                        # Year: 3: 5306.04
                                                        # Year: 4: 5412.1608
                                                        # Year: 5: 5520.4040159999995
                                                        # Year: 6: 5630.81209632
                                                        # Year: 7: 5743.4283382464
                                                        # Year: 8: 5858.296905011328
                                                        # Year: 9: 5975.462843111554
                                                        # Year: 10: 6094.972099973786
    year = year + 1