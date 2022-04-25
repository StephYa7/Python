# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой

str_1 = 'Привет мир. Привет не мир Приветауц'
str_2 = 'Привет'

count = 0

str_1 = str_1.split(' ')

# for i in str_1:
#     if i == str_2:
#         count += 1

# print(count)

for i in range(len(str_1)):
    if str_1[i] == str_2:
        count += 1
print(count)


