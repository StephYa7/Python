# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

list = []

n = int(input('Введите число: '))
summ = 0
f = 0

for i in range(1, n+1):
    f = (1+1/i)**i
    list.append(f)
print(list)

for i in list :
    summ +=i
print(summ)