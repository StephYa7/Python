# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


list = [1, 1]
list2 = [0, 1]

x = int(input())

for i in range(x):
    list.append(list[i]+list[i+1])
    list2.append(list2[i]-list2[i+1])
list2.append(list2[i+1]-list2[i+2])

# i = 1
# while x > 0:
#     list.append(list[i]+list[i+1])
#     list.insert(0, (list[i]-list[i+2]))
#     x -= 1
#     i += 2
# print(list)

list2.reverse()
list2 = list2 + list

print(list2)
