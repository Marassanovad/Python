
import interface as console
import csv_creater as csv

console.Interface("Welcome")
while(True):
    console.Interface("Menu")
    i = int(input('Введите выбранный пункт: '))
    match i:
        case 1: 
            #import
            csv.imp()
            console.Interface("End")
            if(int(input('Введите выбранный пункт: ')) == 2): 
                print("Программа завершила работу")
                break
        case 2:
            # #export
            csv.exp()
            console.Interface("End")
            if(int(input('Введите выбранный пункт: ')) == 2): 
                print("Программа завершила работу")
                break
        case 3:
            print('Запущен выход из программы')
            break
        case _: print("Нет данных")