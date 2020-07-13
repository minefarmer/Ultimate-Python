import Newton

# print(Newton.sqrt(9))  # 3.00009155413138

def square(number):
    print('not from the newton module')
    return number * number

num = 12
print('Square from newton module')  # Square from newton module
print(Newton.square(num))  # 144
print('Square from main program: ')  # Square from main program: 
                                    # not from the newton module
print(square(num))  # 144
