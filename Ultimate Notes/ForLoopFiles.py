# removes empty line with end=''  14
# compute the average of a group of grades 17
# 
# 
# 
# inFile = open('text.txt', 'r')
# line = inFile.readline()
# while(line):
#     print(line)  # this is line 1
#
#                #    this is line 2
#     line = inFile.readline()

# for line in open('text.txt'):
#     print(line, end='')

sum = 0
count = 0
for grade in open('grades.txt'):
    print(grade, end='')  # 100
                            # 93
                            # 87
                            # 72
                            # 66
sum = sum + int(grade)
count = count + 1
average = sum / count
print('Average: ' + str(average))  # Average: 83.6