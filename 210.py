# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах


start = [1, 2, 3, 5, 1,1, 5, 3, 10]
end = []

for i in range(len(start)):
    count=0
    for q in range(i+1,len(start)):
        if start[i] == start[q]:
            print (i,q)
            count+=1
            i=+1
            if count<2:
                end.append(start[i])

print(end)