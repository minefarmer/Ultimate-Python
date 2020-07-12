def square(number):
    return number * number

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def sum(x,y):
    return x + y

# numbers = [1,2,3]  # [1, 2, 3]
# print(numbers)
# numberssq = list (map(square, numbers))
# print(numberssq)  # [1, 4, 9]
# numbers = list(range(1,11))
# print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(even, numbers))
# print(evens)  # [2, 4, 6, 8, 10]
import functools
numbers = list(range(1,11))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = functools.reduce(sum, numbers)
print('The sum is of the range is ' + str(sum))  # The sum is of the range is 55