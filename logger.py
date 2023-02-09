import csv

def add_new(contact):
    try:
        with open('phonebook.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{contact}')
        with open('phonebook.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' ')])
    except FileNotFoundError:
        with open('phonebook.txt', 'w', encoding='utf-8') as book:
            book.write(f'{contact}')
        with open('phonebook.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' ')])

def get_base():
    with open('phonebook.txt', 'r', encoding='utf-8') as book:
        return book.read()