# Calcular temperatura de grados Celcius a grados Farenheit de un rango de valores introducidos por el usuario.
# Formula: centigrados = (farenheit - 32) * 5 / 9


import os

while(True):
    
    os.system("cls")
    print("Calcular temperatura de grados Celcius (°C) a grados Farenheit (°F) de un rango de valores introducidos por el usuario.\n")
    
    
    
    ti= float(input("Temperatura Inicial:  "))
    tf= float(input("Temperatura   Final:  " ))

    c= ti

    print("\n° C\t° F")
    print ("-"*15)
    
    while c<=tf:
        print(f"{c}\t{c*9/5 +32:.2f}")
        c+=1

    print ("-"*15)

    res=input("\nDeseas continuar (S/N): ")
    if res.upper()=='N':
        break

print("\nProceso terminado...")