# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
from datetime import datetime
import time

start_time = datetime.now()

list = []
N = int(input('Введите число: '))

t = 1

for i in range(1,N+1):

    t *= i
    list.append(t)

print(list)

# list.append(1)                                 Так быстрее
# for i in range(1, N):
#     list.append(list[i-1]*(i+1))

# print(list)

time.sleep(0)
print(datetime.now() - start_time)