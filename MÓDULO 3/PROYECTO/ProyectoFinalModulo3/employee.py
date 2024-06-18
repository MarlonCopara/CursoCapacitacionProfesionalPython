class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Nombre: {self.name}\nSalario: {self.salary:.2f}"


class RegularEmployee(Employee):
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("El salario no puede ser negativo.")
        super().__init__(name, salary)


class Manager(Employee):
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("El salario no puede ser negativo.")
        super().__init__(name, salary)

    def get_details(self):
        details = super().get_details()
        return details + "\nPuesto: Gerente"
