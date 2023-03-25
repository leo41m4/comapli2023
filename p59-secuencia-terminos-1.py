# Imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma.

n= int(input('\nDame un numero ? '))
r=0
x=1
for i in range (1, n+1):
        
        print(f'1/{i}! + ', end=' ')
        r+=(1/i)
    
print("\nLa suma es: ",r)
print("\nProceso Terminado")



