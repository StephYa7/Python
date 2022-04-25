# Сложить числа вещественного числа

# num = 43.573
# rez = 0
# while num % 1 != 0:
#     num *= 10

# num = int(num)
# num = str(num)

# for i in num:
#     i = int(i)
#     rez = rez + i

# print(f'Сумма = {rez}')


num = 654654.6519684
num = str(num)
sum = 0
for i in num:
    if i != '.':
        sum += int(i)
print(sum)
