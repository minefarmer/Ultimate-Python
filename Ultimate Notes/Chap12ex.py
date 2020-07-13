# Exercise  1  5
# Exercise  2  17


# def countLetters(words):
#     if len(words) < 1:
#         return 0
#     else:
#         return len(words[0]) + countLetters(words[1:])
    
# sentence = ['now', 'is', 'the', 'time', 'for', 'all', 'good', 'people']
# print(sentence)  # ['now', 'is', 'the', 'time', 'for', 'all', 'good', 'people']
# print(countLetters(sentence))  # 28



# Exercise 2
# in my humble opinion
# IMHO

def first(word):
    return word[0]

# words = ['in','my','humble','opinion']
# acro = list(map(first, words))
# print(acro)  # ['i', 'm', 'h', 'o']


# words = ['in','my','humble','opinion']
# acro = ''
# acro = acro.join(list(map(first, words)))
# print(acro)  # imho


# words = ['in','my','humble','opinion']
# acro = ''
# acro = acro.join(list(map(first, words))) .upper()
# print(acro)  # IMHO


def acronym(words):
    acro =''
    acro = acro.join(list(map(first, words))) .upper()
    return acro

words = ['in','my','humble','opinion']
acro = acronym(words)
print(acro)  # IMHO