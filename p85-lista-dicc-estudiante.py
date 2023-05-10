
grupo = [
    {'nombre':'carlos', 'edad':45, 'carrera':'Sistemas','promedio':9.0},
    {'nombre':'rocio', 'edad':35, 'carrera':'Contabilidad','promedio':10.0},
]

print(grupo, len(grupo))

while True:
    datos = {}
    nombre= input('nombre')
    if nombre=='':
        break
    else:
        datos['nombre'] = nombre
        datos['edad']=int(input('edad: '))
        datos['carrera']=input('carrera: ')
        datos['promedio']=float(input('promedio: '))
        grupo.append(datos)

print(grupo, len(grupo))

print('\nDatos en forma de tabla')
for k in grupo[0].keys(): 
    print(f'{k}\t', end='')

print('\r')

for alumno in grupo: 
    for v in alumno.values(): #ciclos anidados
        print(f'{v}\t', end='')
    print('\r')

# calcular suma de edades
s=0
sp=0
for alumno in grupo:
    s=s+alumno['edad']
    sp= sp + alumno ['promedio']
    
p=s/len(grupo)
pp = sp/len(grupo)

print('\nResumen:')
print(f'Edad:   suma {s}, promedio {p}')
print(f'Promedio:  {sp}, promedio {pp}')


