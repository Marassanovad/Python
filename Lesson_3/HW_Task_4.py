# 4.* Задайте список из произвольных вещественных чисел,
#  количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random


def magic_list(n):
    if n < 0:
        return print("Все плохо")
    ls = [0]*n
    for i in range(n):
        ls[i] = round(random.uniform(0, 10), 2)
    print(ls)
    return ls


def average(list):
    for i in range(len(list)):
       list[i] = round(list[i] % 1, 3)

    print(max(list))
    print(min(list))
    print(max(list)-min(list))


num = int(input("Введите число: "))
average(magic_list(num))


