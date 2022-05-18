# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите '))

list = [randint(0, 10) for i in range(k+1)]  

res = [f'{list[i]}*x^{len(list)-i-1}' for i in range(len(list)-1) if list [i] !=0]
res.append(str(list[len(list)-1]))



print(list)
print(' + '.join(res) + ' = 0')

data = open ('202.txt' , 'a')
data.write(' + '.join(res) + ' = 0\n')
data.close