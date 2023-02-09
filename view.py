def search_inf():
    return input('Введите информацию для поиска: ')

def choose_mode():
    return input ('Выбереите:\n 1 - создать новый контакт,\n 2 - поиск,\n 3 - показать справочник,\n 4 - выход из справочника\n ')


def new_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер контакта: ")
    return f'{last_name} {first_name} {phone_number}'

def show_found (result):
    print ('Результаты поиска: ')
    for i in result:
        print(i)