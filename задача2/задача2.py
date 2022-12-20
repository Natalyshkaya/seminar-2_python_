# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Введите число N')
n = int(input())
factorial = 1
print('Для N=',n, end=": ")
for i in range(1, n):
    factorial = factorial * i
    print(factorial, end=', ')
print(factorial * n)