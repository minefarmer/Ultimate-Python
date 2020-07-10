# inFile = open('text.txt', 'r')
# line = inFile.readline()
# print(line)  # this is line 1
# line = inFile.readline()
# print(line)  # this is line 2
count = 0
total = 0
inFile = open('grades.txt', 'r')
grade = inFile.readline()
while (grade):
    print(grade)
    count = count + 1
    total = total + int(grade)
    grade = inFile.readline()
print('average: ' + str(average))  # 100

                                    # 93

                                    # 87

                                    # 72

                                    # 66