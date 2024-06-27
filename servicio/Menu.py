from dominio.Empleado import Empleado
from interfaz.EmpleadoDAO import EmpleadoDAO
from logcon import log


class Menu:
    # Metodo estático para listar empleado e imprimirlos en la consola.
    @staticmethod
    def listar():
        log.info("Listando empleados")
        for empleado in EmpleadoDAO.listar_empleados():
            print(empleado)
        log.info("Listado de empleados finalizado")

    # Metodo estático para buscar un empleado por su id e imprimirlo en la consola.
    @staticmethod
    def buscar(id):
        log.info("Buscando empleado con id: " + id)
        empleado = EmpleadoDAO.buscar_empleado(id)
        if empleado is None:
            print("No se encontro el empleado con el id: " + id)
        else:
            print(empleado)
        log.info("Buscado de empleado finalizado")

    # Metodo estático para agregar un empleado e imprimir su id en la consola.
    @staticmethod
    def agregar():
        log.info("Agregando empleado")
        try:
            nombre = input("Ingrese el nombre del empleado: ")
            apellido = input("Ingrese el apellido del empleado: ")
            edad = int(input("Ingrese la edad del empleado: "))
            salario = float(input("Ingrese el salario del empleado: "))
            id = EmpleadoDAO.insertar_empleado(nombre, apellido, edad, salario)
            print("El empleado con ID " + str(id) + " se agrego correctamente")
            log.info("Empleado agregado")
        except TypeError:
            print("Error en los datos ingresados")
            log.error(TypeError)
