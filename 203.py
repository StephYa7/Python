# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
# 1111*x^5 + 33*x^3 + 2*x^2 + 144*x^1 = 0
# 3*x^5 + 3*x^4 + 9*x^3 + 2*x^1 + 10 = 0
import re

path = '202.txt'
data = open(path, 'r')

enter = []

for line in data:
    enter.append(line)
data.close()

list1 = enter[0]
list2 = enter[1]




list1 = re.split(r'\s+', re.sub(r'[*x^+=]', ' ', list1).strip())
list2 = re.split(r'\s+', re.sub(r'[*x^+=]', ' ', list2).strip())
itog = []

if len(list1) % 2 != 0:
    list1.append('0')
if len(list2) % 2 != 0:
    list2.append('0')

for i in range(1, len(list1), 2):
    for q in range(1, len(list2), 2):
        if list1[i] == list2[q]:
            itog.append(int(list1[i-1]) + int(list2[q-1]))
            itog.append(int(list1[i]))
            list1[i] = '-'
            list1[i-1] = '-'
            list2[q] = '-'
            list2[q-1] = '-'

for i in range(1, len(list1), 2):
    if list1[i] != '-':
        itog.append(int(list1[i-1]))
        itog.append(int(list1[i]))
for q in range(1, len(list2), 2):
    if list2[q] != '-':
        itog.append(int(list2[q-1]))
        itog.append(int(list2[q]))

for i in range(1,len(itog),2):
    if itog[i] == 0:
        itog.append(itog[i-1])
        itog.append(0)
        itog.pop(i)
        itog.pop(i-1)

for i in range(0,len(itog)-2,2):
    print("{}*x^{} + " .format(itog[i],itog[i+1]),end='')
print(f'{itog[len(itog)-2]} = {itog[len(itog)-1]} ')

