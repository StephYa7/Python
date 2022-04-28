# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел


str = '30 3 6 455 23 7 8 3 21 64 4'

# str = list(str.split(' '))
# str = list(map(int,str))

# min = str[0]
# max = str[0]

# for i in range(len(str)):
#     if str[i] > max :
#         max = str[i]
#     if str[i] < min :
#         min = str[i]

# print(max)
# print(min)


# print(f'Максимальное число: {max}  Минимальное число  {min}')

str002 =[]
for i in str.split():
    str002.append(int(i))

print(max(str002), min(str002) )



