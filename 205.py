# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя




# start = [1, 5, 2, 3, 4, 6, 1, 7]
# bestLen = 0
# interim = []
# end = []
# listmin =[]
# indexF = 0
# indexS = 0

# def rek (rangeleft,rangeright)


    


num_list = [1, 6, 7, 8, 3, 4, 6, 8, 11, 1, 9, 7, 4, 1, 1, 3, 8, 2, 5, 9]
res_list =[]
for j in range(len(num_list)-1):
    index = j
    temp_list = [num_list[j]]
    while index < len(num_list) - 1:
        rem_list = [i for i in num_list[index:] if i > temp_list[-1]]
        if len(rem_list) !=0:
            current_min = min(rem_list)
        else:
            break
        temp_list.append(current_min)
        index += num_list[index:].index(current_min)
    print(temp_list)
    if len(temp_list) > len(res_list):
        res_list = temp_list.copy()
print (res_list)