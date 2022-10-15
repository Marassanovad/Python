import user_interface as console
import calculator as cal


console.Interface("Welcome")
while(True):
    console.Interface("Menu")
    i = int(input('Введите выбранный пункт: '))
    match i:
        case 1: 
            print('Калькулятор для работы с рациональными числами')
            cal.Calc_rat(input("Введите выражение: "))
            console.Interface("End")
            if(int(input('Введите выбранный пункт: ')) == 2): 
                print("Программа завершила работу")
                break
        case 2:
            print('Калькулятор для работы с комплексными числами')
            console.Interface("Action")
            i = input('Введите знак: ')
            print(cal.Calc_comp(i))
            console.Interface("End")
            if(int(input('Введите выбранный пункт: ')) == 2): 
                print("Программа завершила работу")
                break
        case 3:
            print('Запущен выход из программы')
            break
        case _: print("Нет данных")