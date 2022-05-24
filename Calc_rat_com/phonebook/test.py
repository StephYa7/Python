import io

path = 'Calc_rat_com\phonebook\Phone_book_line.xls'            # Загрузка
data = io.open(path, 'r',encoding='utf-8')
for line in data:
    print(line)
data.close()







