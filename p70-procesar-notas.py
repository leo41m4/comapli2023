#  Leer n notas hasta introducir un 0. Las notas pueden estar entre 0 y 100 (validar).
# Imprime: cuantas notas, las notas, suma, promedio, notas menores al promedio y cuantas son, nota máxima y nota mínima


import os;os.system('cls')

notas = []
n=1
suma=0
promedio=0


while n!=0:
    n=float(input('Notas: '))
    if n>0 and n <100:
        notas.append(n)
        suma = suma + n
    elif n!=0:
        print("ERROR - LA NOTA NO ESTA EN EL RANGO")

print('Fin')

promedio=suma/len(notas)

print(f'Se capturaron  : {len(notas)} Notas')
print('Las Notas son  : ',notas)
print('\nESTADISTICAS ')
print('\nSuma       : ',suma)
print('Promedio   : ',promedio)
print('Mayor      : ',max(notas))
print('Menor      : ',min(notas))

menosp =[]
for n in notas:
    if n < promedio:
        menosp.append (n)

print('\nMenores que el promedio  : ',len(menosp))
print('Estos son : ',menosp)

print('Mayor: ', max(notas))
print('Menor: ', min(notas))

print('\nProceso terminado...')