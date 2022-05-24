import io

def search(line):
    path = 'Calc_rat_com\phonebook\Phone_book_line.xls'            # Загрузка
    data = io.open(path, 'r',encoding='utf-8')

    if line == 1:
        name = input('Введите Фамилию: ')
        for line in data:
            line = line.split(',')
            if line[0] == name:
                print(line)
    data.close()
    if line == 2:
        name = input('Введите Имя: ')
        for line in data:
            line = line.split(',')
            if line[1] == name:
                print(line)
    data.close()
    if line == 3:
        name = input('Введите Номер телефона: ')
        for line in data:
            line = line.split(',')
            if line[2] == name:
                print(line)
    data.close()



print(search(1))