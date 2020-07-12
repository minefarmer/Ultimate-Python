# anonymous function
# Lambda form

# def square(number):
    # return number * number
    
# square = lambda x: x*x
# print(square(2))  # 4
numbers = [1,2,3,4]
numberssq = list(map(lambda x:x*x, numbers))
print(numberssq)  # [1, 4, 9, 16]