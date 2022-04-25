# Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды 


second = int(input('Введите кол-во секунд'))


day = 0
hour = 0
minute = 0


day = int(second /86400)
hour = int((second % 86400) / 3600)
minute = int(((second % 86400) % 3600) / 60)
second =int(((second % 86400) % 3600) % 60)
print(f'Дней {day},Часов {hour},Минут {minute},Секунд {second}')