# Напишите программу, удаляющую из текста все слова содержащие "абв".

text = 'п укдлпукпуклмидьук укапкуп куа кп кабв уакабвабвабв абв  енуеабв  акупукрбв  абууубав  ваб'


# text= text.split()

# def delT(tex,x):
#     list =[]
#     for i in range(len(tex)):
#         if x not in tex[i]:
#              list.append(tex[i])
#     return list

# print(text:=delT(text,'абв'))

string = list(filter(lambda x: 'абв' not in x, text.split()))
result = " ".join(string)
print(result)
