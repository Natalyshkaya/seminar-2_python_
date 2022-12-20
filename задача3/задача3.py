#Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

print('Введите число N')
n = int(input())
dict = {}
sum = 0
print('Для N=',n, end=": ")
for i in range(1, n+1):
    dict[i] = round((1 + (1 / i))**i, 2)
    sum = sum + dict[i]
print(dict)
print('Сумма=',sum)