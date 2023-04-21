import os;os.system('cls')

nums = []
n=0
suma=0
promedio=0

print ('Introduce calificaciones entre 0 y 10. Usa 99 para terminar\n')

while n!=99:
    n=float(input('Numero > '))
    if n>=0 and n <=10:
        nums.append(n)
        suma = suma + n
    else:
        print('x')

print('< Fin')

promedio=suma/len(nums)

print('Se capturaron    : ',len(nums))
print('Los numero son   : ',nums)
print('\nEstadisticas   : ')
print('Suma       : ',suma)
print('Promedio   : ',promedio)
print('Mayor      : ',max(nums))
print('Menor      : ',min(nums))

mp =[]
for n in nums:
    if n > promedio:
        mp.append (n)

print('Mayores que promedio  : ',len(mp))
print('Y son : ',mp)

