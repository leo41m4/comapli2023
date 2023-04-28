
# Leer n nombres de ciudades en una lista hasta introducir $. Imprimir cuantos elementos son, y la lista completa
# Ordenar la lista en orden descendente y mostrar (sort). 
# Imprimir cuantas ciudades inician con la letra consonante (startswith) y sus nombres

import os;os.system('cls')
print('\nIntroducir ciudades hasta teclear $ para terminar ')
a= []
ciudad= ''
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
x = []

while ciudad!='$':
    ciudad = input('Ciudad: ')
    if(ciudad !='$'):
        a.append(ciudad)

print(f'\nTotal: {len(a)} ciudades')
print(f'\nLas ciudades son: ')
print(f'{a}')

print('\nOrdenadas (sort): ')
a.sort()
print(a)
print('\nEn orden descendente: ')
a.sort(reverse=True)
print(a)

for iscons in a:

    if(iscons.lower().startswith(tuple(cons))):
        x.append(iscons)

print(f'\nCiudades que inician con consonante: {len(x)}')
print(f'{x}')

print('\nProceso terminado...')