# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
from ast import Index
from operator import indexOf
import re


from posixpath import split
import string


path = '202.txt'            # Загрузка
data = open(path, 'r')

enter = []

for line in data:
    enter.append(line)
data.close()






list1 = enter[0]
list2 = enter[1]
list1 = re.split(r'\s+', re.sub(r'[*x^ + =]', ' ', list1).strip())
list2 = re.split(r'\s+', re.sub(r'[*x^ + =]', ' ', list2).strip())

itog = []

for i in list1:
    if list1.index(i) % 2 != 0:
        for q in list2:
            if list2.index(q) % 2 != 0:
                if q == i:
                    itog.append(i)
                    itog.append((list1.index(i)-1)+((list2.index(q)-1)))
                    print(i, q)


print(itog)
print(list1)
print(list2)
