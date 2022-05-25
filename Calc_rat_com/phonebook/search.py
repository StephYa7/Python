import io

def search_line(line_search):
    path = 'Calc_rat_com\phonebook\Phone_book_line.xls'            # Загрузка
    data = io.open(path, 'r',encoding='utf-8')

    if line_search == 1:
        name = input('Введите Фамилию: ')
        for line in data:
            sline = line.split(',')
            if sline[0] == name:
                return line
    if line_search == 2:
        name = input('Введите Имя: ')
        for line in data:
            sline = line.split(',')
            if sline[1] == name:
                return line
    if line_search == 3:
        name = input('Введите Номер телефона: ')
        for line in data:
            sline = line.split(',')
            if sline[2] == name:
                return line
    if line_search == 4:
        name = input('Введите слово из заметки: ')
        for line in data:
            sline = line.split(',')
            target = sline[3].split()
            for i in target:
                if i.lower() == name.lower():
                    return line
    data.close()

