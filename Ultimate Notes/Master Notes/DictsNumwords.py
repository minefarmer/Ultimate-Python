sentance = 'now is the time for all good people to come '
sentance += 'to the aid of their party'
words = sentance.split(' ')
words = sorted(words)
print('Sentence in sortrd order:\n')  # Sentence in sortrd order:
print(words)  # ['aid', 'all', 'come', 'for', 'good', 'is', 'now', 'of', 'party', 'people', 'the', 'the', 'their', 'time', 'to', 'to']
numWords = ()
for i in range(0, len(words)):
    if words[i] in numWords:
        numWords[words[i]] += 1
    # else:
    #     numWords[words[i]] = 1  # Traceback (most recent call last):
                                # File "/home/carl/Github/Ultimate-Python/Ultimate Notes/Master Notes/DictsNumwords.py", line 12, in <module>
                                #     numWords[words[i]] = 1
                                # TypeError: 'tuple' object does not support item assignment
    
print('Word list and count: \n')  # Word list and count:
# for key in numWords.keys():  # Traceback (most recent call last):
                        #     File "/home/carl/Github/Ultimate-Python/Ultimate Notes/Master Notes/DictsNumwords.py", line 18, in <module>
                        #     for key in numWords.keys():
                        # AttributeError: 'tuple' object has no attribute 'keys'
# print(key, numWords[key])