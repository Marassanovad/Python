# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]


num = int(input('Enter the number: '))

def easy_num(n):
    i = 2
    while n > 1:
        while n % i == 0:
           print(i, end=' ')
           n //= i
        i +=1

easy_num(num)
        
    

