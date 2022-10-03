# 4.* Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (от 0 до 10) многочлена, записать в файл полученный
#  многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0


import random

k = int(input("Enter the number:"))
polynomial = str()

with open("poly.txt", "a", encoding="utf-8") as output:
    if k > 0:
        output.write(f"Натуральная степень {k} : ")
    while k > 0:
        num = random.randint(0, 10)
        symbol = random.choice(['+', '-'])
        if num != 0 and k > 1:
            output.write(f"{num}*x^{k} {symbol} ")
        if k == 1:
            output.write(f"{num} = 0 \n")
        k -=1





        
            










