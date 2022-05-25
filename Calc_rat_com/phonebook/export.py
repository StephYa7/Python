
def export (file_name):

    imp = file_name
    book = 'Calc_rat_com\phonebook\Phone_book_line.xls'
    imp = open(imp, 'a', encoding='utf-8')
    book = open(book, 'r', encoding='utf-8')
    
    imp.writelines('\n')
    for line in book:
        imp.writelines(line)

# a = 'Calc_rat_com\phonebook\import_line.csv'

# export(a)

