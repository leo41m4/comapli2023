# Generar 2 listas de 10 números aleatorios
# Suma ambas listas en una tercera, suma solo los elementos de cada lista si ambos son impares. Imprime las 3 listas.

import os;os.system('cls')

import random 

a=[]
b=[]
c=[]

print('Generando listas de numeros aleatorios...')

for n in range (10):
    a.append(random.randint(1,100)) 
    b.append(random.randint(1,100)) 

print(f'Lista 1 : {a}')
print(f'Lista 2 : {b}')
print("\nLista 3 (Solo se suman los elementos de cada lista si ambos son impares):")

for i in range(10):
    if((a[i]%2 != 0) and (b[i]%2 != 0)):
        x = a[i] + b[i]
        print(f'[{i+1}]{x} ', end='')
        c.append(x)             

print('\n\nProceso terminado...')