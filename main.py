from create_contact import phonebook_create
from delete_contact import delete_contact
from show_phonebook import *
from change_contact import change

def main():
    flag = True
    while flag:
        doit = int(input('Введите 1, для создания контакта:\n '
                     'Введите 2, для удаления контакта:\n'
                     'Введите 3, для просмотра контактов:\n '
                     'Введите 4, для изменения контактов:\n'
                     'Введите 5, для изменения контакта:\n'
                     'Введите 6, для выхода:\n --> '))
        if doit == 1: phonebook_create()
        elif doit == 2:
            name = input('Введите данные удаляемого контакта: ')
            print(delete_contact(name))
        elif doit == 3: show_contacts()
        elif doit == 4: change()
        elif doit == 5: show_contact_1()
        else:
            flag = False


if __name__ == '__main__':
    main()



