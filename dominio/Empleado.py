# Clase Empleado con atributos id, nombre, apellido, edad y haberes.
class Empleado:
    def __init__(
        self, nombre: str, apellido: str, edad: int, salario: float, id: int = None
    ):
        self._id: int = id
        self._nombre: str = nombre
        self._apellido: str = apellido
        self._edad: int = edad
        self._salario: float = salario

    # Getters
    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def apellido(self) -> str:
        return self._apellido

    @property
    def edad(self) -> int:
        return self._edad

    @property
    def salario(self) -> float:
        return self._salario

    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}, Salario: {self._salario}"


# Prueba de la clase
if __name__ == "__main__":
    empleado1 = Empleado("Juan", "Pérez", 30, 5000.0)
    print(empleado1)
