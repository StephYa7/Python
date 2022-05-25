def import_file (file_name):

    string =''
    imp = file_name
    book = 'Calc_rat_com\phonebook\Phone_book_line.xls'
    imp = open(imp, 'r', encoding='utf-8')
    book = open(book, 'a', encoding='utf-8')
    for line in imp:

        if ',' in line :
            book.writelines(f'\n{line}')
            continue
        if len(line) > 1:
            string+= line
        else:
            string = string.replace('\n', ',')
            book.writelines(f'\n{string}')
            book.writelines('')
            string = '' 
    if len(string) >1:
        string = string.replace('\n', ',')
        book.write(f'\n{string}')