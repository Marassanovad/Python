# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27



a = (input('Введите число: '))
b = len(a)
a = float(a)
sum = 0
a = a*(10**b)
a=str(a)
b=len(a)
a=float(a)
for i in range(b+1):
    ost = 0
    ost = int(a % 10)
    a = a / 10
    sum = sum + ost
    
print("Сумма равна:",sum)

# Second way

n = float(input('Введите вещественное число: '))
sum = 0 
while not n.is_integer(): 
    n = n*10 
    while n != 0: 
        sum += n % 10 
        n //= 10
print(sum)

# print(sum(map(int, list(input("Введите дробное число: ").replace(".", "")))))
