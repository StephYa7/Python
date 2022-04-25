# Написать программу проверки, является ли строка палиндромом

from cgitb import reset


string = '124y yy421'
lenght = len(string) -1
min = 0


while string[min] == string[lenght]:
    if min < lenght:
        min += 1
        lenght -= 1
   
else : print('не')        

        
   
    
    



print(string[8])