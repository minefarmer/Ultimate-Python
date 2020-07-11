# square function   6
# the numVowels function   26
# 
# 
# 
# def  square(number):
#     return number * number

# def numVowels(string):
#     string = string,lower()
#     count = 0
#     for i in range(len(string)):
#         if string[i] == 'a' or string[i] == 'e' or \
#            string[i] == 'i' or string[i] == 'o' or \
#            string[i] == 'u':
#            count += 1 #count = count + 1
#     return count

# print('Enter a number: ')  # 12
# num = int(input())
# numsquared = square(num)
# print(str(num) + ' squared = ' + str(numsquared))  # 12 squared = 144



# the numVowels function
def  square(number):
    return number * number

def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if string[i] == 'a' or string[i] == 'e' or \
           string[i] == 'i' or string[i] == 'o' or \
           string[i] == 'u':
           count += 1 #count = count + 1
    return count

# print('Enter a number: ')  # 12
# num = int(input())
# numsquared = square(num)
# print(str(num) + ' squared = ' + str(numsquared))  # 12 squared = 144
print('Enter a string: ')
string = input()
print('There are ' + str(numVowels(string)) + ' vowels in the string,')