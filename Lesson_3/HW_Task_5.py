# 5. ** Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)

    for i in range(2, n + 1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])

    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, n - 2):
        fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0]))
    return fibo_list



num = int(input("Введите число: "))
print(fibo(num))


