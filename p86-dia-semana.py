
import os; os.system('cls')

dias={1:'Domingo', 2:'Lunes', 3:'Martes', 4:'Miercoles', 5:'Jueves', 6:'Viernes', 7:'Sabado'}

while True:
    dia = int(input('Digite número de día : '))
    if dia > 0 and dia < 8:
        print(f'El dia de la semana es: {dias[dia]}')
        break
    else:
        print('Numero invalido')

print('\nProceso Terminado')