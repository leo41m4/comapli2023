# Leer dos listas con 5 elementos. Multiplica las listas y guárdalos en una tercera lista. 
#Imprime las tres listas

import os;os.system('cls')

a=[]
b=[]
c=[]

n=int(input('Cuantos elementos por Lista: '))

print('\nDame los elementos de la Lista 1 : ')
for i in range (n):
    x=int(input(f'Elemento {i+1} : '))
    a.append(x)


print('\nDame los elementos de la Lista 2 : ')
for i in range (n):
    x=int(input(f'Elemento {i+1} : '))
    b.append(x)

for i in range (n): # Multiplicacion  de la tercer lista
    x= a [i] * b[i]
    c.append(x)

print(f"\nLista 1 {a}")
print(f"Lista 2 {b}")
print(f"Lista 3 {c}")

print('\nProceso terminado...')