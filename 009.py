# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти


print('Введите четверть: ')

x = int(input())



if (x == 1):
    print('x > 0 и y > 0')
if (x == 2):
    print('x < 0 и y > 0')
if (x == 3):
    print('x > 0 и y < 0')
if (x == 4):
    print('x < 0 и y < 0')
