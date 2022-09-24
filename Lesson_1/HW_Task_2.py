# 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# z = int(input('Введите z: '))
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z) == (not x and not y and not z)):
                print(x, y, z)
                print("Утверждение истинно")
            else:
                print(x, y, z)
                print("Утверждение ложно")



