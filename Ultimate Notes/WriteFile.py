outFile = open('text.txt', 'w')  # the first step is to create a file variable, or file object, that associates a physical file on the harddrive with the variable in our programdatetime A combination of a date and a time. Attributes: ()
outFile.write('this is line 1\n')
outFile.write('this is line 2\n')
outFile.close()  # I must close the file. Because when I issue a write function python writes the function to a buffer into memory. The file is written to disk when closeddatetime A combination of a date and a time.  ***  File was created in the Ultimate-Python folder
outFile = open('grades.txt', 'w')
grade = 0
print ('Enter a grade (q to quit): ')
grade = raw_input()
while (grade != 'q'):
    outFile.write(grade + '\n')
    print ('Enter a grade (q to quit): ')
    grade = raw_input()
outFile.close()
        # 100
        # Enter a grade (q to quit): 
        # 93
        # Enter a grade (q to quit): 
        # 87
        # Enter a grade (q to quit): 
        # 72
        # Enter a grade (q to quit): 
        # 66
        # Enter a grade (q to quit): 
        # q
        # (base) carl@lmde:~/Github/Ultimate-Python$ cat grades.txt
        # 100
        # 93
        # 87
        # 72
        # 66