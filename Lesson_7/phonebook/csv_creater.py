import csv



def new():
    with open('phonebook.csv', 'a', newline='') as f:
        fieldnames = ['Имя', 'Фамилия', 'Номер', 'Описание']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'Имя': 'Baked', 'Фамилия': 'Beans', 'Номер': '777', 'Описание': 'aaaa '})
    

def imp():
    with open('phonebook.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def exp():
    with open('phonebook.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow({str(input("Имя: ")): 'Имя', input('Фамилия: '): 'Фамилия',  input('Номер: '): 'Номер', input('Описание:'): 'Описание'})


