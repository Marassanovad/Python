# 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))


leftside = not (x or y or z)
rightside = not x and not y and not z


if leftside == rightside:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")