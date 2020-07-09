answer = 'Watson'
print('Here is a guessing game. You get three tries.')
print('What is the the name of the computer that played on Jeoperdy?')
response = raw_input()
if response == answer:
    print('That is right!')
else:
    print('Sorry. Guess again: ')
    response = raw_input()
    if response == answer:
        print('That is right!')
    else:
        print('Sorry. One more guess: ')
        response = raw_input()
        if response == answer:
            print('That is right!')
        else:
            print('Sorry. No more guesses. the answer is ' + answer + ',')