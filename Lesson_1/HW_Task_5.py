# 5. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
#AB = √(xb - xa)2 + (yb - ya)2

x1 = int(input('Введите X1: '))
y1 = int(input('Введите Y1: '))

x2 = int(input('Введите X2: '))
y2 = int(input('Введите Y2: '))

AB=((x2-x1)**2+(y2-y1)**2)**0.5
print(f'{AB:.3f}')