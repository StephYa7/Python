# Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;
''

string = '5-8/2*3+4*3-7*1-8+5*8-8+8-9*9+5*5-5-5*5+8*8+9-9+1-9+9*9-3*3'
start = []

for i in string:
    if i.isdigit() == True:
        start.append(int(i))
    elif i == '+':
        start.append('+')
    elif i == '-':
        start.append('-')
    elif i == '*':
        start.append('*')
    elif i == '/':
        start.append('/')

buf = []

for i in range(len(start)):
    if i == len(start):
        break
    if start[i] == '*' or start[i] == '/':
        if start[i] == '*':
            res = start[i-1] * start[i + 1]
            start.pop(i-1)
            start[i] = res
            buf.pop(-1)
            buf.append(res)
            continue
        else:
            res = start[i-1] / start[i+1]
            start.pop(i-1)
            start[i] = res
            buf.pop(-1)
            buf.append(res)
            continue
    buf.append(start[i])

print(buf)

for j in range(len(buf)):
    if j == len(buf):
        break
    if buf[j] == '+' or buf[j] == '-':
        if buf[j] == '+':
            res = buf[j-1]+buf[j+1]
            buf[j+1] = res
        else:
            res = buf[j-1] - buf[j+1]
            buf[j+1] = res
print(buf)

print(res)