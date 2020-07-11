# iter and next  12
# display the first element # 1  14
# display the first element # 2  17  (best way)
# A file object is an iterator   28
# 
# numbers = [1,2,3,4,5]
# for number in numbers:
#     print(number)
    
    
    
numbers = [1,2,3]
it =iter(numbers)
#  display the first element # 1
# print(it.__next__())  # 1

#  display the first element # 2
# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3  ***** inside a for loop the StopIteration will automatically happen
# print(next(it))  # Traceback (most recent call last):
#                 # File "c:/Users/pgold/MatsonHub/Ultimate-Python/Ultimate Notes/Iterators.py", line 21, in <module>
#                 #     print(next(it))  # 3
#                 # StopIteration 
                
                
                
# A file object is an iterator
fileIt = open('grades.txt', 'r')  # this is a file iterator
print(next(fileIt))  # 100
                    #             ***  a new line added to file
print(next(fileIt), end='')
