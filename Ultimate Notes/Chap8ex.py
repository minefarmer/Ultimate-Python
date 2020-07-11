# Exercize 1   6
# Exercise 2   20
# 
# 
# 
# # 5! = 5*4*3*2*1 = 120
# # 6! = 6 * 5!
# # factorial computation iteratively
# print("Enter a number: ")  # Enter a number:
# num = int(input())  # 5
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
# print(str(num) + '! = ' + str(fact))  # 5! = 120





bar = ""
for grade in open('grades.txt'):
    for i in range(1, int(grade) + 1):
        if i % 5 == 0:
            bar = bar + "*"
    print(bar, i)
    bar = ""