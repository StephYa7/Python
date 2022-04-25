# Напишите программу, которая выводит нечетные числа из заданного списка и останавливается, если встречает число 554.

# from ast import IfExp


a = [2, 3, 5, 6, 8, 556, 255, 554, 66, 53]

for i in a :
    if i == 554 :
        break
    if i % 2 != 0 :
        print(i, end = ' ')


# number = 0
# list = []
# while number != 554:
#     number = int(input('Введите число: '))
#     if number % 2 != 0:
#         list.append(number)
# print(list)
