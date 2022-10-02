# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

import random


def random_list(count):
    if count < 0:
        return print("Все плохо")

    ls = random.sample(range(count * 2), count)
    print(ls)
    return ls


def new_list(ls):

    newLength = int(len(ls) / 2 + len(ls) % 2)
    mult = []
    for i in range(0, newLength):
        mult.append(ls[i] * ls[len(ls) - 1 - i])
    if len(ls) % 2 != 0:
        mult[-1] = ls[newLength-1]
        return mult
    return mult


num1 = int(input("Введите число: "))


print(new_list(random_list(num1)))
