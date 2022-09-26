# * 4. Напишите программу, которая принимает на вход 2 числа.
#  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15




n = int(input('Number of elements: '))
ls = list()

pos1 = int(input('Position one: '))
pos2 = int(input('Position two: '))
sum=1


for k in range(-n,n+1):
    
    ls.append(k)
    if pos1==k+1 or pos2==k+1:
        sum*=ls[k]


print(ls)
print("Произведение равно: ",sum)
