# Standard for loop  7
# For loop with the index by indexing into the list.   21
# Accessing some partial set of the complete list.   39
# 
# 
# 
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)  # 1
#                     # 2
#                     # 3
#                     # 4
#                     # 5
#                     # 6
#                     # 7
#                     # 8
#                     # 9
#                     # 10


# For loop with the index by indexing into the list   *****************************
# numbers = [1,2,3,4,5,6,7,8,9,10]
# # for number in numbers:
# # print(number)  
# # numbers[0]
# for i in range(0, len(numbers)):
#     print(numbers[i])  # 1
#                         # 2
#                         # 3
#                         # 4
#                         # 5
#                         # 6
#                         # 7
#                         # 8
#                         # 9
#                         # 10


#  Accessing some partial set of the complete list.  ***************************
numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
# print(number)
for i in range(0, len(numbers),2):
    print(numbers[i])  # 1
                        # 3
                        # 5
                        # 7
                        # 9
                        
numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
# print(number)
for i in range(0, len(numbers),3):
    print(numbers[i])  # 1
                        # 4
                        # 7
                        # 10
                   