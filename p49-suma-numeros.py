# Suma y promedio de n números introducidos por el usuario: 

print('Suma y promedio de n números introducidos por el usuario:') 
n = int(input('Cuantos numeros ? '))
s = 0

for x in range(1,n+1):
    print(f'Numero {x}: ', end=' ') 
    num = float(input())
    s += num
print(f'\nSuma: {s} y el promedio es: {s/n:.2f} ')

print('\nProceso terminado')