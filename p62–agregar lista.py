# Agregar elementos a la lista 
import os; os.system('cls')

print('Agregar elementos a una lista existente \n') 
nums = [80.3, 12.5, 60.2, 30.4]
print(f'Todos los números : {nums} - {len(nums)} \n') 
nums.append(90)
nums.append(100)
print(f'Agregar al final de la lista : {nums}\n') 
nums.insert(5,80)
print(f'Insertar : {nums}\n') 
otros = [110,120,130]
nums.extend(otros)
print(f'Extender lista : {nums}\n')