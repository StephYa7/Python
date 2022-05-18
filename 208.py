# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
count = 0
a = '11'
b = '12'
c = '13'
d = '21'
e = '22'
f = '23'
g = '31'
h = '32'
i = '33'
print('Введите координаты куда хотите поставить крестик или нолик: ')

while not a == c == b or d == e == f or g == h == i or a == d == g or b == e == h or c == f == i or a == e == i or c == e == g:

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
            a = ' x'
        elif x == b:
            b = ' x'
        elif x == c:
            c = ' x'
        elif x == d:
            d = ' x'
        elif x == e:
            e = ' x'
        elif x == f:
            f = ' x'
        elif x == g:
            g = ' x'
        elif x == h:
            h = ' x'
        elif x == i:
            i = ' x'
    else:
        if x == a:
            a = ' o'
        elif x == b:
            b = ' o'
        elif x == c:
            c = ' o'
        elif x == d:
            d = ' o'
        elif x == e:
            e = ' o'
        elif x == f:
            f = ' o'
        elif x == g:
            g = ' o'
        elif x == h:
            h = ' o'
        elif x == i:
            i = ' o'
    count +=1
