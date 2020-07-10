numbers = {'Cynthia':'2356', 'Raymond':'2345', 'David':'2373'}
print(numbers['Cynthia'])  # 2356
print(numbers.keys())  # dict_keys(['Cynthia', 'Raymond', 'David'])
print(numbers.values()) # dict_values(['2356', '2345', '2373'])
for key in numbers.keys():
    print(key + " extension is: " + numbers[key])  # Cynthia extension is: 2356
                                                    # Raymond extension is: 2345
                                                    # David extension is: 2373
