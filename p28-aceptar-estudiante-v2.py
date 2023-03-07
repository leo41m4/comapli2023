# Dado el nombre del estudiante, su edad y tres calificaciones, decidir si el estudiante es aceptado.

import os
os.system("cls")

print("Aceptar un estudiante en base al sexo, la edad y tres calificaciones: \n")
nombre=input("Dame tu nombre: ")
op=input("Elige la opción [H]ombre o [M]ujer segun corresponda: ").upper()
edad=int(input("Dame tu edad: "))
if op== "H":
    print("\nEsta Universidad es solo para mujeres")
elif op=="M":
    print("")
    if edad <21:
        print("\nNo aceptamos menores 21 años de edad")
    elif edad >=21:
        print("Dame tres calificaciones separadas por enter\n")
        c1, c2, c3=float(input()), float(input()), float(input())
        prom=(c1+c2+c3)/3
        if prom <8:
            print("\nNo aceptamos un promedio de calificaciones menor a 8")
        elif prom>=8 and prom<=9.5:
            print(f"\n{nombre} Bienvenida a la Universidad Kitty Kat SA, tu edad es de {edad} años y el promedio de tus calificaciones es {prom:.2f} estas aceptada")
        elif prom >=9.5:
            print("\nFuera de Rango")
else:
    print("\nOpcion invalida")

print("\nProceso Terminado")