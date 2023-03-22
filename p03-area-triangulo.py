# Calcular el area de un triangulo

print("Calcular el area de un triangulo\n")
print("Dame la base y la altura separados por enter:")
base, altura =int(input()), int(input()) #aqui se leen dos datos en un sola linea, hay que dar enter entre cada uno

area = base*altura /2

print(f"El triangulo de base {base} y altura {altura} tiene una area de {area}")