import os;os.system('cls')

dia=''
por=0
dias=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
paga=[100,200,300,400,500,600,700]

while True:
    dia=input('Dame un dia entre lunes y domingo ?  ') 
    if dia in dias:
        break

print('\nElegiste el dia: ',dia)
pos=dias.index(dia)

print('La paga es: ',paga[pos])