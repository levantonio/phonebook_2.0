
def show_contacts():
    with open('phonebook.txt', 'r') as data:
        contacts = data.readlines()
        for line in contacts:
            print(line)

def show_contact_1():
    name = input('Введите имя контакта: ')
    with open('phonebook.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if name.lower() in line.lower():
                print(line)

show_contact_1()