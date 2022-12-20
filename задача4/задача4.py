import random
print('Введите строку текста')
str = input()
strList = list(str)
print(strList)
random.shuffle(strList)
print(strList)