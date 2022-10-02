# 1. Задайте список, состоящий из произвольных чисел,
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8

from itertools import product
import random


def random_list(count, num):
    if count < 0 :
        return print("Все плохо")

    ls = random.sample(range(count * 2), count)
    print(ls)
    if num == 1:
        sum = 0
        for i in range(0, count, 2):
            sum += ls[i]
        print(sum)
    elif num ==2 :
        sum = 1
        for i in range(1, count, 2):
            sum += ls[i]
        print(sum)
    else:
        print('Все плохо')


num1 = int(input("Введите число: "))
num2 = int(input("Введите 1-если число нечетное или 2- если четное: "))
random_list(num1, num2)
