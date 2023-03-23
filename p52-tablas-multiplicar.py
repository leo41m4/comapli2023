#Imprimir las tablas de multiplicar desde la tabla del 1, hasta la tabla n


n=int(input('Hasta que tabla quieres ?  '))
m=int(input('Hasta donde             ?  '))

for i in range (1, n+1):
    print(f"\nTabla del {i}")
    for j in range (1, m+1):
        print(f'{i}  x {j} = {i*j}')


print('\nProceso Terminado')
    
