# We want to use a for-loop anytime we want to process the elements of a sequence, especially when we want to process all of the elements in a sequence.
# part 1  5
# part 2  28

# for i in [1,2,3,4,5]:
#     print(i)  # 1
#             # 2
#             # 3
#             # 4
#             # 5

# numbers = [1,2,3,4,5]
# for x in numbers:
#     print(x)  # 1
#             # 2
#             # 3
#             # 4
#             # 5
            
# numbers = [1,2,3,4,5]
# sum =0
# for x in numbers:
#     sum = sum + x
# print(sum)  # 15



#  part 2  **********************************************
# word =  'hello'
# for letter in word:
#     print(letter)  # h
#                     # e
#                     # l
#                     # l
#                     # o

sentence = 'now is the time for all good people to come to the aid.'
count= 0
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' \
        or letter == 'u':
        count = count + 1
print('The number of bowels is ' + str(count))  # The number of bowels is 19