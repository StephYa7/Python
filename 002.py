#Найти максимальное из пяти чисел

t = [1, 4, 2, 5, 6, 7, 4, 5, 15, 66, 2, 33]
max = 0
for i in t:
    if i > max:
        max = i
print(max)
