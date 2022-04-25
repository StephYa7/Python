# Посчитайте, сколько раз символ встречается в строке.

string = 'grejlkghoih goire gnhoerbnmoern tg'
symbol = 'r'
sum = 0

for i in string:
    if i == symbol:
        sum += 1

print(sum)