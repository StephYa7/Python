# Найти сумму чисел списка стоящих на нечетной позиции



a = [0, 1, 2, 3, 4, 5, 6, 100]

itog = 0

for i in range(len(a)):
    if i % 2 != 0:
        itog += a[i]
print(itog)
