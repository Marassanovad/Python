# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


import random


def magic_list(n):
    if n < 0:
        return print("Negative value of the number of numbers!")
    ls = []
    for i in range(n):
        ls.append(random.randint(0, 10))
    print(ls)
    return ls

def sor_num(ls):
    new_ls = []
    for i in range(len(ls)):
        s = ls.count(ls[i])
        if s == 1:
            new_ls.append(ls[i])
    print(new_ls)

def sor_num2(ls):
    new_ls2 =[]
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j and ls[i] == ls[j]:
                break
        else:
            new_ls2.append(ls[i])
    print(new_ls2)
    
num = int(input("Введите число: "))
print('First way: ')
sor_num(magic_list(num))

print('Second way: ')
sor_num2(magic_list(num))



