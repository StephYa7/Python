# Реализовать алгоритм перемешивания списка.

import random

list = [5, 6, 8, 22, '33r', 55, 'ww']

# for i in range(0, len(list)):

#     x = list[i]
#     list.pop(i)
#     list.append(x)

# print(list)

i = 100
while i > 0:

    a = random.randint(0, len(list)-1)
    x = list[a]
    list.pop(a)
    list.append(x)
    i -= 1

print(list)
