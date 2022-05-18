# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
# Вставить и перезаписать.

from posixpath import split

path = '204.txt'            # Загрузка
data = open(path, 'r')
enter = data.read().split()
data.close()

enter.sort()

for i in range(len(enter)-1):
    if int(enter[i]) != int(enter[i+1])-1:
        print(enter[i])
        enter.insert(i+1, int(enter[i])+1)

print(enter)
