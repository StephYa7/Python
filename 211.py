# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

start = [1, 2, 3, 5, 1, 5, 3, 10]
end = []

q = start[0]
count = 0

for i in range(len(start)):
    if count == 1:
        end.append(start[i-1])
    count = 0
    for q in range(len(start)) :
        if start[q] == start[i]:
            count +=1
if count == 1:
    end.append(start[i-1])
            
print(end)


