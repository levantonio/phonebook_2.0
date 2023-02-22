from delete_contact import delete_contact
from show_phonebook import show_contacts


def change():
    change = int(input('Введите 1, для изменения имени: \n'
                        'Введите 2, для изменения фамилии: \n'
                        'Ввудите 3, для изменения отчества \n'
                        'Введите 4, для изменения номера: \n'
                        'Введите 5, для отмены действия: \n'))

    with open('phonebook.txt', 'r') as file:
        lines = file.readlines()
        print(show_contacts())
        name = input('Введите имя изменяемого контакта : ')
        for line in lines:
            if name.lower() in line.lower():
                data = line.split(' ')
                if change == 1:
                    new_line = [line.replace(data[0], input('Введите новое имя: ').capitalize())]
                    new_lines = lines + new_line
                    with open('phonebook.txt', 'w') as f:
                        f.writelines(new_lines)
                elif change == 2:
                    new_line = [line.replace(data[1], input('Введите новую фамилию: ').capitalize())]
                    new_lines = lines + new_line
                    with open('phonebook.txt', 'w') as f:
                        f.writelines(new_lines)
                elif change == 3:
                    new_line = [line.replace(data[2], input('Введите новое отчество: ').capitalize())]
                    new_lines = lines + new_line
                    with open('phonebook.txt', 'w') as f:
                        f.writelines(new_lines)
                elif change == 4:
                    new_line = [line.replace(data[3], input('Введите новый номер : ').capitalize())]
                    new_lines = lines + new_line
                    with open('phonebook.txt', 'w') as f:
                        f.writelines(new_lines)
        delete_contact(name)
        print('Успешно')






