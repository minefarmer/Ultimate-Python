import math
# Part 1  5
# Part 2 == simplify 36
# 
# Part 1
# def square(number):
#     return number * number

# def sqrt(number):
#     return sqrtHelper(1.0, number)

# def sqrtHelper(guess, number):
#     if (closeEnough(guess, number)):
#         return guess
#     else:
#         return sqrtHelper(improve(guess, number), number)
    
# def closeEnough(guess, number):
#     return (math.fabs((square(guess)) - number) < 0.001)

# def improve(guess, x):
#     return average(guess, (x / guess))

# def average(x, y):
#     return (x + y) / 2

# print(sqrt(144))  # 12.000000012408687







#  Part 2
def average(x, y):
    return (x + y) / 2

def square(number):
    return number * number

def sqrt(number):
    def closeEnough(guess):
        return (math.fabs((square(guess)) - number) < 0.001)
    def improve(guess):
        return average(guess, (number / guess))
    def sqrtHelper(guess):
        if (closeEnough(guess)):
            return guess
        else:
            return sqrtHelper(improve(guess))
    return sqrtHelper(1.0)

# print(sqrt(9))  # 3.00009155413138
print(sqrt(144))  # 12.000000012408687