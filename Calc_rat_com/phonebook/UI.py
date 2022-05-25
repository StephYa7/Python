from search import *
from import_phonebook import import_file
from new_phone import *
from export import *

def start():

    command = int(input(
        'Введите номер операции из списка: 1 = поиск, 2 = дополнение, 3 = импорт, 4 = экспорт.\n:'))

    if command == 1:
        a = int(input(
            'Введите номер по какому полю необходим поиск: 1 = Фамилия, 2 = Имя, 3 = Телефон, 4 = Описание.\n:'))
        print(search_line(a))
   
    if command == 2:
        add_sername = input('Введите Фамилию: ')
        add_name = input('Введите Имя: ')
        add_phone = input('Введите телефон: ')
        add_note = input('Введите заметку: ')

        new_phone(add_sername,add_name,add_phone,add_note)

    if command == 3:
        a = input('Введите адрес файла из которого производирть импорт: ')

        import_file(a)

    if command == 4:
        a=input('Введите адрес куда перенести информацию: ')
        export(a)
        
