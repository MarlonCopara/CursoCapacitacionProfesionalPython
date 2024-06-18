# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass  # Método genérico para hacer sonido

    def detalles(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Clase derivada Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau!"

    def detalles(self):
        detalles_animal = super().detalles()
        return f"{detalles_animal}, Raza: {self.raza}"

# Clase derivada Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "¡Miau!"

    def detalles(self):
        detalles_animal = super().detalles()
        return f"{detalles_animal}, Color: {self.color}"

# Crear instancias de Perro y Gato
mi_perro = Perro("Fido", 5, "Labrador")
mi_gato = Gato("Mittens", 3, "Gris")

# Acceder a métodos y atributos de las instancias
print(mi_perro.detalles())  # Imprime: Nombre: Fido, Edad: 5, Raza: Labrador
print(mi_perro.hacer_sonido())  # Imprime: ¡Guau!
print(mi_gato.detalles())  # Imprime: Nombre: Mittens, Edad: 3, Color: Gris
print(mi_gato.hacer_sonido())  # Imprime: ¡Miau!
