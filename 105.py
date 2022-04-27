# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

list = []

n = int(input("Введите число: "))

for i in range(-n, n+1):
    list.append(i)

print(list)

summ = 1
path = 'file.txt'            # Загрузка
data = open(path, 'r')       # Загрузка

for index in data:
    summ *= list[int(index)]
data.close()


print(summ)