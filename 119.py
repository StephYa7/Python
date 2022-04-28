# Составить список простых множителей натурального числа N

x = int(input('Введите число: '))
y = 1
z = []

for i in range(1, x):
    if x % i == 0:
        z.append(i)

print(z)
