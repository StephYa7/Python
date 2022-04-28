# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
import math

a = [2, 3, 4, 5, 6]
new =[]

# q = 0
# w = len(a) -1

# while q <= w:
#     new.append(a[q]*a[w])
#     q+=1
#     w-=1
# print(new)



# for i in range(math.ceil((len(a)/2))):
#     new.append(a[i] * a[len(a)-1-i])

# print(new)

for i in range((len(a)+1)//2):
    new.append(a[i] * a[len(a)-1-i])

print(new)
