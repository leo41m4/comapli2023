import os;os.system('cls')

estudiante = {
    'Nombre:': 'Juan Perez',
    'Edad:':45,
    'Email:':'jperez@msn.com',
    'Carrera:':'Sistemas'
}

print(estudiante, len(estudiante),'\n')

estudiante['Calificacion:'] = 9.5

print(estudiante, len(estudiante),'\n')

estudiante['Email:'] = 'jperez@gmail.com'

print(estudiante, len(estudiante),'\n')

estudiante.update({'Sexo:':'Hombre','Semestre:':'7'})

print(estudiante, len(estudiante),'\n')

for k in estudiante.keys():
    print(k)
print()

for v in estudiante.values():
    print(v)
print()

for k,v in estudiante.items():
    print(k , v)

print('\nProceso terminado...')



