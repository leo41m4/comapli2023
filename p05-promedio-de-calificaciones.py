# Calcular el promedio de 3 calificaciones 

print('Calcular el promedio de 3 calificaciones:\n')
print('Dame 3 calificaciones separadas por espacios:') 

c1,c2,c3 =input().split()
c1,c2,c3 =[float(c1), float(c2),float(c3)] 
prom = (c1+c2+c3)/3
print(f'El promedio de : {c1},{c2},{c3} es {prom}')