from Newton import average, square

# # num1 = 199
# # num2 = 78
# # print('The average is ' + str(average(num1, num2)))  # The average is 138.5

# num1 = 199
# num2 = 78
# print('The average is ' + str(average(num1, num2)))  # The average is 138.5
# print(sqrt(9))  # Traceback (most recent call last):
#                 # File "/home/carl/Github/Ultimate-Python/Ultimate Notes/NewtonTest2.py", line 10, in <module>
#                 #     print(sqrt(9))
#                 # NameError: name 'sqrt' is not defined


# the solution is below

num1 = 199
num2 = 78
# print('The average is ' + str(average(num1, num2)))  # The average is 138.5
# print(sqrt(9)) 
avg = average(num1, num2)
print('The average is ' + str(avg))  # The average is 138.5
print('The squre of the average is ' + str(square(avg)))  # The squre of the average is 19182.25