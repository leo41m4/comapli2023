# - Llenar un lista con los primeros n números impares (ej 1 3 5 7 9 11 n). Calcular e imprimir la suma y promedio de los números. 
# - Mostrar los números que son divisibles entre 3 y sumarlos. Pedir un elemento a buscar en la lista original y decir si esta y en que posición

import os; os.system('cls')

impar = []
impardivtres = []
nuimpar = 0
sum = 0
suma = 0
prom = 0

n = int(input('Numeros Impares (Lista): '))

while len(impar) != n:
    nuimpar = nuimpar + 1
    if(nuimpar%2 != 0):
        impar.append(nuimpar)
        sum = sum + nuimpar
print(impar)
prom = sum/len(impar)
print(f'Suma      : {sum}')
print(f'Promedio  : {prom}')

for  i in impar:
    if (i%3 == 0):
        impardivtres.append(i)
        suma = suma + i

print(f'\nNumeros divisibles entre 3: ')
print(f'{impardivtres}')
print(f'Suma : {suma}')

while True:
    x = int(input('\nQue elemento buscas de la lista original (Salir "999"): '))
    if x in impar:
        print(f'El numero {x} se encuentra en la posición {impar.index(x)} de la lista original.')
    elif(x == 999):
        break
    else:
        print('Este numero no se encuentra en la lista.')
print('\nProceso terminado...')
