# Iterators cannot return both the key and value  *** keys only   14
# using a for loop   22
# 
# 
# 
grades = {'Cynthia':88, 'David':77, 'Claton':99}
# for key in grades.keys():
#     print(key, grades[key])  # Cynthia 88
#                             # David 77 
#                             # Claton 99



# Iterators cannot return both the key and value  *** keys only
# it = iter(grades)
# print(next(it))  # Cynthia
# print(next(it))  # David
# print(next(it))  # Claton



#  using a for loop
for key in grades:
    print(key, grades[key])  # Cynthia
                            # David
                            # Claton