# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

data = 'wwweregerrrrg444443grdf3ggggggggggggrerg33333333eeqqq'
newdata = ''
first = ''
count = 1

for i in data:
    if i != first:
        if first != '':
            newdata += str(count)+first
        count = 1
        first = i
    else:
        count += 1
newdata += str(count)+data[-1]
print(newdata)
