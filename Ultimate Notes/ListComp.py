# The idea of list comprehension is to take this two statement loop and simplify it.   13
# Example; two lowercase   21
# not list comprehension with files   30
# strip the new lines - list comprehension with files   40  ******************
# Including an if statment in list comprehension   46
# Print the length of all the words in this sentence   53

# grades = [71, 81, 77, 84]
# for i in range(len(grades)):
#     grades[i] = grades[i] + 5
# print(grades)  # [76, 86, 82, 89]

# The idea of list comprehension is to take this two statement loop and simplify it.
# grades = [71, 81, 77, 84]
# print(grades)  # [71, 81, 77, 84]
# grades = [grade + 5 for grade in grades]
# print(grades)  # [76, 86, 82, 89]



#  Example two lowrcase
# words = ['NOW', 'IS', 'THE', 'TIME']
# print(words)  # ['NOW', 'IS', 'THE', 'TIME']
# words = [word.lower() for word in words]
# print(words)  # ['now', 'is', 'the', 'time']
# print(words)



# not list comprehension
# file = open('grades.txt')
# grades = file.readlines()
# print(grades)  # ['100\n', '93\n', '87\n', '72\n', '66\n']
# for i in range(len(grades)):
#     grades[i] = grades[i].rstrip()  # removes the newline  ************
# print(grades)  # ['100', '93', '87', '72', '66']



# strip the new lines - list comprehension with files
# grades = [grade.rstrip() for grade in open('grades.txt')]
# print(grades)  # ['100', '93', '87', '72', '66']



# List comp exercise  *** including an if statment in list comprehension
# N = range(1,101)
# EN = [x for x in N if x % 2 == 0]
# print(EN)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]



# Print the length of all the words in this sentence
sent = 'now is the time for all good people to come to the aid '
sent += 'of the party'
words = sent.split(' ')
wlen = [(word, len(word)) for word in words]
for i in wlen:
    print(i)  # ('now', 3)
            # ('is', 2)
            # ('the', 3)
            # ('time', 4)
            # ('for', 3)
            # ('all', 3)
            # ('good', 4)
            # ('people', 6)
            # ('to', 2)
            # ('come', 4)
            # ('to', 2)
            # ('the', 3)
            # ('aid', 3)
            # ('of', 2)
            # ('the', 3)
            # ('party', 5)
    