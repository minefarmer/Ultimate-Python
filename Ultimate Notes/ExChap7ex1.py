# Exercise 1  4
# Exercise 2  21

# tries = 0
# answer = 'Watson'
# while(tries <= 3):
#     print('What is the the name of the computer that played on Jeoperdy?')
#     response = raw_input()
#     tries = tries + 1
#     if (response =='Watson'):
#         print('That is right!')
#         break
#     elif (tries == 3):
#         print('Sorry. The answer is Watson')
#         break
#     else:
#         print("Sorry. Try again.")
    
    
    
op1 = 0.0
op2 = 0.0
op = ''
while op1 != 'q':
    print('Enter first number (q to quit: ')
    op1 = raw_input()
    if op1 == 'q':
        break;
    op1 = float(op1)
    print('Enter second number: ')
    op2 = float(raw_input())
    print('Enter an operation (+,=, *,/)')
    op = raw_input()
    if (op == '+'):
        print(op1 + op2)
    elif op == '-':
        print(op1 - 2)
    elif op == '*':
        print(op1 * op2)
    elif op == '/':
        print(op1 / op2)
    else:
        print('Did not recognize operator.')
            # Enter first number (q to quit: 
            # 2
            # Enter second number: 
            # 2
            # Enter an operation (+,=, *,/)
            # +
            # 4.0
            # Enter first number (q to quit: 
            # 23
            # Enter second number: 
            # 11
            # Enter an operation (+,=, *,/)
            # -
            # 21.0
            # Enter first number (q to quit: 
            # 4.4
            # Enter second number: 
            # 1.1
            # Enter an operation (+,=, *,/)
            # *
            # 4.84
            # Enter first number (q to quit: 
            # 144
            # Enter second number: 
            # 12
            # Enter an operation (+,=, *,/)
            # /
            # 12.0
            # Enter first number (q to quit: 
            # q