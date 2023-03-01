# Calcula la segunda ley de Newton (Fuerza, Masa y Aceleración)

import os
os.system("cls")

print("Calcula la segunda Ley de Newton (Fuerza, Masa y Aceleracion)\n")
print("[F]uerza      (f=m*a)")
print("[M]asa        (m=f/a)")
print("[A]celeracion (a=f/m)\n")
op=input("Elige la opción F, M, o A segun corresponda: ").upper()

if op=="F":
    print("\nCalculando la fuerza...")
    m=int(input("\nDame la masa        ? "))
    a=int(input("\nDame la aceleración ? "))
    f= m * a
    print(f"\nLa Fuerza es {f}")
elif op== "M":
    print("\nCalculando la Masa...")
    f=int(input("\nDame la fuerza      ? "))
    a=int(input("\nDame la aceleración ? "))
    m= f / a
    print(f"\nLa Masa es {m}")
elif op== "A":
    print("\nCalculando la Aceleración...")
    f=int(input("\nDame la fuerza     ? "))
    m=int(input("\nDame la masa       ? "))
    a= f / m
    print(f"\nLa Aceleracion es {a}")
else:
     print("\nOpción Invalida")

print("\nProceso Terminado")
