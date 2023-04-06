# Iterar sobre los elementos de la lista 
import os; os.system('cls')

nums = [2, 4, 6, 8, 10, 12, 14, 16] 
print(f'Todos los números : {nums}')

print('\nIterar por elementos de la lista forma 1: ') 
for n in nums:
    print(n, end=" ")
    
print('\nIterar por los elementos de la lista forma 2 : ') 
for i in range(len(nums)):
    print(nums[i],end=" ")
    
print('\nMostrar cada elemento de la lista sumando 2: ') #no afecta la lista de los elementos
for n in nums:
    print(n+2,end=" ")
print(f"\n{nums} ") # Se observa el efecto.

print('\nModificar la lista sumando 10 a cada elemento: ') # si va a afectar la lista de los elemenntos principal. diferencia entre las dos formas.
for i in range(len(nums)):
    nums[i]=nums[i] + 10
print(f"\n{nums} ")