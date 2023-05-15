
import os; os.system('cls')

caracter = {}

x = input('Palabras: ')

for a in x:
    if a in caracter:
        caracter[a] = 1 + caracter[a]
    else:
        caracter[a] = 1

print(f'{caracter}')

print('\nProceso Terminado')