from datetime import date

def phonebook_create():
    day = date.today()
    flag = True
    while flag:
        print(f'Создание новой записи')
        last_name = input('Введите фамилию: ')
        name = input('Введите имя: ')
        patronomyc = input('Введите отчество:')
        number = input('Введите номер: ')
        with open('phonebook.txt', 'a') as f:
            f.write(f'{name.capitalize()} {last_name.capitalize()} {patronomyc.capitalize()} {number} , create {day}\n')
            print('успешно')
        qwestion = input('Хотите ли вы записать еще номера нажмите Y/N: ')
        if qwestion.upper() == 'N':
            flag = False









