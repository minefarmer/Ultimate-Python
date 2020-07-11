def isVowel(letter):
    if letter == 'a' or letter == 'e' or \
       letter == 'i' or letter == 'o' or \
       letter == 'u':
       return True
    else:
        return False


def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if isVowel(string[i]):
           count += 1 
    return count

# print('Enter a number: ')  # 12
# num = int(input())
# numsquared = square(num)
# print(str(num) + ' squared = ' + str(numsquared))  # 12 squared = 144
print('Enter a string: ')  # Enter a string:
string = input()  # hello world
print('There are ' + str(numVowels(string)) + ' vowels in the string,')  # There are 3 vowels in the string,