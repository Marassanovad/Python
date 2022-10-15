import random


#создание листа n-размера с рандомными числами от 0 до 20
def create_list(n):
    num = [random.randint(0,21) for i in range(n) ]
    return num

