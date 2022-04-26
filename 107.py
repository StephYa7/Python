# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел


from datetime import datetime

a = datetime.now()

a = int(a.microsecond)

print(a)

max= int(input("Введите максимальное число рандома: "))

if max < 11:
    a = str(a)
    b = a[-1]
    print(b)

while a > max:
    if a % 3 == 0:
        a = a**0.5
    if a % 2 == 0:
        a = a/2
    if a % 5 == 0:
        a = a/3  
    else : a = a/3

print(int(a))