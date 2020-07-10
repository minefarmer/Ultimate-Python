# Finding the longest word  16
# 
# 
# 
# numbers = (1,2,3,4,5)
# sum = 0
# for num in numbers:
#     sum = sum + num 
#     print(num)  # 1
#                 # 2
#                 # 3
#                 # 4
#                 # 5
# print('the sum is ' + str(sum))  # the sum is 15

# Finding the longest word  ****************************
words = ("now","is","time","the")
for word in words:
    print(word)  # now
                # is
                # time
                # the
max = 0
for i in range(1, len(words)):
    if len(words[i]) > len(words[max]):
        max = i
print('The longest word is ' + words[max])  # The longest word is time
