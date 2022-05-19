# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
count = 0
a = '11' ; b = '12'; c = '13'; d = '21'; e = '22'; f = '23'; g = '31'; h = '32'; i = '33'
print('Введите координаты куда хотите поставить крестик или нолик: ')

while not (a == c == b or d == e == f or g == h == i or a == d == g or b == e == h or c == f == i or a == e == i or c == e == g):

    print(f' {a}  |  {b}  |  {c} ')
    print('     |      |     ')
    print('------------------')
    print(f' {d}  |  {e}  |  {f} ')
    print('     |      |     ')
    print('------------------')
    print(f' {g}  |  {h}  |  {i} ')
    print('     |      |     ')

    x = input()
    if count % 2 == 0:

        if x == a:
            a = ' X'
        elif x == b:
            b = ' X'
        elif x == c:
            c = ' X'
        elif x == d:
            d = ' X'
        elif x == e:
            e = ' X'
        elif x == f:
            f = ' X'
        elif x == g:
            g = ' X'
        elif x == h:
            h = ' X'
        elif x == i:
            i = ' X'
    else:
        if x == a:
            a = ' O'
        elif x == b:
            b = ' O'
        elif x == c:
            c = ' O'
        elif x == d:
            d = ' O'
        elif x == e:
            e = ' O'
        elif x == f:
            f = ' O'
        elif x == g:
            g = ' O'
        elif x == h:
            h = ' O'
        elif x == i:
            i = ' O'
    count += 1

    if count == 9:
        print('Ниья')
        break
if count % 2 == 0:
    print('O Победил')
else:
    print('X Победил')
