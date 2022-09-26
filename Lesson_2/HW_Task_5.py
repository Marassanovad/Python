# 5. ** Реализуйте алгоритм перемешивания списка. 
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]


#не доделано!!!

import random

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ranNum=0
b = [0 for i in range(10)]

for i in range(len(b)):
    ranNum=a[random.randint(0, 9)]
    if ranNum not in b:
        b[i]=ranNum
    
# random.shuffle(b)
print(a)
print(b)