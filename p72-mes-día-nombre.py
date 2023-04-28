# Leer un número de mes (ej 4). Imprimir: días del mes, y nombre del mes (ej marzo, 30).
# Asume 28 para febrero, guarda días en una lista, y nombres de mes en otra.


import os;os.system('cls')

pos=0
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
dias = [31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    pos=int(input('Teclea entre 1 y 12 para el mes: '))
    if pos>= 0 and pos <=12:
        break
    else:
        print('Error de rango')
        
print(f'\nElegiste el mes: ({meses[pos-1]},{dias[pos-1]})')      

print('\nProceso terminado...')
