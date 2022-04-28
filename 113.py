# Написать программу преобразования десятичного числа в двоичное




number = int(input())
n=''
while number!=0:
    n=str(number%2)+n
    number//=2
print(n)