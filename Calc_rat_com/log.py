from datetime import datetime as dt

def example_log(input,out):
    with open('Calc_rat_com/log_example.csv', 'a') as file:
        time = dt.now().strftime('%D:%H:%M')
        file.write('{}  Вводили пример: {}  итог: {}\n'.format(time,input,out))

