# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
# for(int max = 1; number > max; max= max *10){

#     ost = n % 10;
#     n= n / 10;
#     sum = sum + ost;
# }


a = (input('Введите число: '))
b = len(a)
a = float(a)
sum = 0
a = a*(10**b)
# x = a.split(".")
# a = int(x[0]) # целая часть
# b = int(x[1]) # дробная часть
for i in range(b+1):
    ost = 0
    ost = int(a % 10)
    a = a / 10
    sum = sum + ost
    
print("Сумма равна:",sum)
