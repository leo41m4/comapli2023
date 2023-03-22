# Calcular el promedio de 5 calificaciones, para luego evaluar el resultado y enviar un mensaje de acuerdo al promedio.
import os
os.system("cls")

print("Calcular el promedio de 5 calificaciones y enviar un mensaje de acuerdo al promedio\n")
print('Dame 5 calificaciones separadas por espacios:\n') 

c1,c2,c3,c4,c5 =input().split()
c1,c2,c3,c4,c5 =[float(c1), float(c2),float(c3), float(c4), float(c5)] 
prom = (c1+c2+c3+c4+c5)/5
print(f'\nEl promedio de las calificaciones es: {prom}')

if prom >=0 and prom <=6:
    print(f"\nEstas Reprobado")
elif prom >=6.1 and prom <=7:      
    print(f"\nPasas de Panzazo")
elif prom >=7.1 and prom <=8:
    print(f"\nMuy bien, a mejorar")
elif prom >=8.1 and prom <=9:
    print(f"\nExcelente sigue asi")
elif prom >=9.1 and prom <=10:
    print(f"\nPerfecto tu esfuerzo valió la pena")

else:
    print("\nNúmero fuera de rango")
    
print("\nProceso terminado")