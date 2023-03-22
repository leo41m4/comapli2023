# Imprime numeros del 100 a 1 con for

print('\nNumeros del 100 a 1 con for') 

print('\n')
n = int(input("Hasta donde: "))
s = int(input("Paso       : "))

for num in range(n,0,-s):
    print(num,end=' ')

print('\n\nGracias por utilizar este programa')