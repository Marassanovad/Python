# 2. Напишите программу, которая на вход принимает 5 чисел
#  и находит максимальное из них.

minN = 0

for i in range(5):
    print('Введите число: ')
    a = int(input())
    if minN < a:
        minN = a

print('Большое число: {minN}')

