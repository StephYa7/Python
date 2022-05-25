
def new_phone(family,name,phone,note):
    
    path = 'Calc_rat_com\phonebook\Phone_book_line.xls'            # Загрузка
    data = open(path, 'a',encoding='utf-8')

    data.writelines(f'\n,{family}')
    data.writelines(f',{name}')
    data.writelines(f',{phone}')
    data.writelines(f',{note}')



