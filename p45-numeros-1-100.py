# Imprime numeros del 1 a 100 con for

print('\n')
n = int(input("Hasta donde: "))
s = int(input("Paso       : "))
print('\nNumeros del 1 al 100 con for') 

for x in range(1,n+1,s):
    print(x,end=' ')

print('\n\nGracias por utilizar este programa')