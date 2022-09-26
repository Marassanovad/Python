# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


n = int(input('Введите число: '))
ls = list()
a=int(1)
sum=int(0)

for k in range(1,n+1):
    a=round((1+1/k)**k)
    sum+=a
    ls.append(a)

print(ls)
print(sum)

