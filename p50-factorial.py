# Imprimir el factorial de un numero

n=int(input("Dame un numero? "))

f=1

for i in range (1, n+1):
    print(f"{i} ", end= " x ")
    f=f*i

print(f"\nEl Factorial es: {f}")
