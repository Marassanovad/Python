# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, 
# без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

def bin_num(a):
    result = []
    while a != 0:
        result.append(a % 2)
        a = a//2
    result.reverse()
    return result


num = int(input("Введите число: "))
print(*bin_num(num))
