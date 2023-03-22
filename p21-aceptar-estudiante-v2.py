# Aceptar un estudiante en base a su edad y sus calificaciones

import os
os.system("cls")

print("Aceptar un estudiante en base a su edad y sus calificaciones: \n")
nombre=input("Dame tu nombre: ")
edad=int(input("Dame tu edad: "))

if edad >=18:
    print("Dame dos calificaciones separadas por enter\n")
    c1, c2=int(input()), int(input())
    if c1>=8 and c2>=8:
        print(f"\n{nombre} Bienvenido a la universidad, tu edad es {edad} y tus calificaciones son {c1} y {c2} lo permiten")
    else:
        print("\nNo aceptamos calificaciones menores a 8") 
else:
  print("\nNo aceptamos menores de edad")
    
print("\nProceso Terminado")
