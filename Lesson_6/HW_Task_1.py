# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
#  значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

import random

# print([(x,y) for x in ["apple","pie"] for y in [6,7,8,9,10]])



def create_list(n):
    num = [random.randint(0,20) for i in range(n) ]
    return num


def greater_than_the_previous_element(ls):
    greater = [j for i, j in zip(ls, ls[1:]) if j > i]
    return greater

a = create_list(int(input('Введите число: ')))
print(a)
print(greater_than_the_previous_element(a))