# Написать программу проверки, является ли строка палиндромом


string = '1234534321'
lenght = len(string) -1
min = 0


while min < lenght:
    if string[min] != string[lenght]:
       quit(f'{string} Не палиндром')
    min += 1
    lenght -= 1



print('Палиндром')        


        
   
    
    



