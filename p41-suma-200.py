# Calcular la suma de numeros introducidos por el usuario, hasta que la suma sea >= 200.
while True:
    import os
    os.system("cls")

    print("Calcular la suma de numeros introducidos por el usuario, hasta que la suma sea >= 200.")

    cuenta=0
    suma=0

    while True: 

        num=float(input("\nNúmero: "))
        if num !=0:
            cuenta = cuenta + 1
            suma=suma+num
        if suma >= 200:
        
            break
        
    print("\nResumen: ")
    print(f"\nSe capturaron: {cuenta} números")
    print(f"\nLa suma es: {suma}")
    
    res=input('\nDeseas Continuar (S/N): ') 
    if res.upper()=='N':
        break

print("\nProceso terminado...")