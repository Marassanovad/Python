# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.
# Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
# in
# 424
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147,
# 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280,
# 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

def create_list(n):
    num = [i for i in range(20 ,n+1)]
    return num


def multiple(ls, del1=20, del2=21):
    new_ls = [n for n in ls if n%20 == 0 or n%21 == 0]
    return new_ls

a = create_list(int(input('Введите N: ')))
# print(a)
print(multiple(a))