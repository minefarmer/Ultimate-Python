def ftoc(temp):
    return (temp - 32.0) * (5.0 / 9.0)

def ctof(temp):
    return temp * (9.0 / 5.0) + 32.0

def convert(temp, toScale):
    if toScale.lower() == 'c':
        return ftoc(temp)
    else:
        return ctof(temp)
        
print('Enter a temperatre: ')
temp = int(input())
print('Enter the scale to convert to: ')
scale = input()
convertedtemp = convert(temp, scale)
print(temp, convertedtemp, scale)