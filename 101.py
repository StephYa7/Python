# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


list = []

N = int(input('Введите число'))
T = 1

while N > 0:
    list.append(T)
    T *= -3
    N -= 1

print(list)


# list = []
# N =1 
# count = int(input('Введите число'))

# for i in range(count):
#     list.append(N)
#     N*=-3
# print(list)