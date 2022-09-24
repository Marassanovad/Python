# 1. Напишите программу, которая принимает на вход два числа
#    и проверяет, является ли одно число квадратом другого.


print('Введите число a:')
a = int(input())

print('Введите число b:')
b = int(input())

if a*a==b: print('квадрат a равен b')
elif b*b==a: print('квадрат b равен a')
else : print('не равно')


# a = int(input())
# b = int(input())
# if a * a == b or b * b == a:
#     print("yes")
# else:
#     print("no")