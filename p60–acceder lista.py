# Acceder a los elementos de una lista 

import os; os.system('cls')

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99, 100]
print('Acceder a los elementos de una lista\n')
print(f'Tamaño de la lista : {len(nums)} \n')
print(f'Todos los números : {nums} \n')
print(f'Primero y último : {nums[0]}, {nums[-1]} \n')
print(f'Del 30 al 60 : {nums[2:6]} \n')
print(f'Los primeros 3 : {nums[:3]} \n')
print(f'Los últimos 3 : {nums[7:]} \n')