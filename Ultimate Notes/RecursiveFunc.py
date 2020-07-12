# recursion 1   5
# recursion 2   20


# # 5! = 5 * 4 * 3 * 2 * 1
# # 5! = 5 * 4!
# def fact(number):
#     if number <= 1:
#         return 1
#     else:
#         return number * fact (number-1)
    
# print(fact(5))  # 120
# # print(fact(10)) # 3628800





#  recursion 2
# explode('hello')->'h e l l o'
# def explode(word):
#     if len(word) <= 1:
#         return word
#     else:
#         return word[0] + ' ' + explode(word[1:])
    
# print(explode('hello'))  # h e l l o


# removeDups('aabbcc') ->'abc"
def removeDups(word):
    if len(word) <= 1:
        return word
    elif word[0]==word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])
  
word = 'aabbbccccdd'
print(word)
print(removeDups(word))