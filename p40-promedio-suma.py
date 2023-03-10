# Calcular la suma y el promedio de una serie de numeros introducidos por el usuario, hasta salir con 0.
while True:
    import os
    os.system("cls")

    print("Calcular la suma y el promedio de una serie de numeros introducidos por el usuario, hasta salir con 0. ")

    c=0
    s=0

    while True:
        n=float(input("\nNúmero: "))
        if n !=0:
            c = c + 1
            s=s+n
        else:
            break

    print("\nResumen:")
    print(f"\nSe capturaron {c} números")
    print(f"\nLa suma es: {s}")
    print(f"\nEl promedio es: {s/c} ")

    res=input('\nDeseas Continuar (S/N) ? ') 
    if res.upper()=='N':
        break

print("\nProceso terminado...")
    