# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect

import random


def create_list(num, a: str = 'абв'):
    ls = []
    for i in range(num):
        letter = random.sample(a,3)
        ls.append("".join(letter))
    return " ".join(ls)  

def delete_word(ls):
    ls = ls.replace('абв', '')
    return ls
    
list =create_list(int(input('Введите число: ')))
print(list)
print(delete_word(list))