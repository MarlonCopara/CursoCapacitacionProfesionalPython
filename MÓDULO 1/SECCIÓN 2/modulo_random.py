import random

# Número aleatorio entre 0 y 1
numero_aleatorio = random.random()
print(f"Número aleatorio entre 0 y 1: {numero_aleatorio}")

# Número entero aleatorio entre 1 y 10
entero_aleatorio = random.randint(1, 10)
print(f"Número entero aleatorio entre 1 y 10: {entero_aleatorio}")

# Elección aleatoria de una lista
eleccion_aleatoria = random.choice(['manzana', 'banana', 'cereza'])
print(f"Elección aleatoria de una lista: {eleccion_aleatoria}")
