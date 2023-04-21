
import os;os.system('cls')

nombres=[]
edades=[]
pos=0
may=0

print('Introduce nombres y edades utiliza * para terminar:  \n')

while True:
    nombre=input('Nombres: ')
    if nombre=='*':
        break
    else:
        nombres.append(nombre)
        edad=int(input('Edad: '))
        edades.append(edad)

print(nombres)
print(edades)

for i in range (len(nombres)):
    if edades[i] >=18:
        print(f'\nMayor de 18: {nombres[i]} {edades[i]}')

may=max(edades)
pos=edades.index(may)

print(f'\n"Edad Mayor" Nombre: {nombres[pos]}, Edad: {edades[pos]}')