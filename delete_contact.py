
def delete_contact(name):

    with open('phonebook.txt', 'r') as file:
        lines = file.readlines()

        data = ''
        for line in lines:
            if name.lower() in line.lower():
                del line
            else:
                data += line

    with open('phonebook.txt', 'w') as f:
        f.writelines(data)
        return (f'контакт - {name} успешно удален!!!')



