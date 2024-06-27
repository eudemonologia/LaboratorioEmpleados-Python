# Clase Empleados que funciona como interfaz entre la vista y el modelo
from servicio.Conexion import Conexion
from dominio.Empleado import Empleado
from logcon import log


class EmpleadoDAO:

    _SELECCIONAR = "SELECT * FROM empleados WHERE id = ?"
    _SELECCIONAR_TODOS = "SELECT * FROM empleados"
    _INSERTAR = (
        "INSERT INTO empleados (nombre, apellido, edad, salario) VALUES (?, ?, ?, ?)"
    )
    _ACTUALIZAR = "UPDATE empleados SET nombre = ?, apellido = ?, edad = ?, salario = ? WHERE id = ?"
    _ELIMINAR = "DELETE FROM empleados WHERE id = ?"

    @classmethod
    def listar_empleados(cls) -> list:
        with Conexion():
            Conexion.crear_consulta(cls._SELECCIONAR_TODOS)

        empleados = Conexion.respuesta
        empleados = [Empleado(id=empleado[0], *empleado[1:]) for empleado in empleados]
        return empleados

    @classmethod
    def buscar_empleado(cls, id) -> Empleado:
        empleado = []
        with Conexion():
            Conexion.crear_consulta(cls._SELECCIONAR, id)

        empleado = Conexion.respuesta
        empleado = Empleado(id=empleado[0][0], *empleado[0][1:]) if empleado else None
        return empleado

    @classmethod
    def insertar_empleado(cls, nombre, apellido, edad, salario) -> Empleado:
        with Conexion():
            Conexion.crear_consulta(
                cls._INSERTAR,
                nombre,
                apellido,
                edad,
                salario,
            )

        return Conexion.respuesta

    @classmethod
    def actualizar_empleado(cls, empleado: Empleado):
        with Conexion():
            Conexion.crear_consulta(
                cls._ACTUALIZAR,
                empleado.nombre,
                empleado.apellido,
                empleado.edad,
                empleado.salario,
                empleado.id,
            )

        log.info(f"Empleado {empleado.nombre} actualizado")
        return Conexion.respuesta

    @classmethod
    def eliminar_empleado(cls, empleado):
        with Conexion():
            Conexion.crear_consulta(cls._ELIMINAR, empleado.id)
            id_eliminado = Conexion.enviar_consulta()
            log.debug(f"Empleado {empleado.nombre} eliminado")
            return id_eliminado
