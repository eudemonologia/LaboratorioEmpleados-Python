# Clase Empleados que funciona como interfaz entre la vista y el modelo
from servicio.Conexion import Conexion
from dominio.Empleado import Empleado
from logcon import log


class EmpleadoDAO:

    _SELECCIONAR = "SELECT * FROM empleados"
    _INSERTAR = (
        "INSERT INTO empleados (nombre, apellido, edad, salario) VALUES (?, ?, ?, ?)"
    )
    _ACTUALIZAR = "UPDATE empleados SET nombre = ?, apellido = ?, edad = ?, salario = ? WHERE id = ?"
    _ELIMINAR = "DELETE FROM empleados WHERE id = ?"

    @classmethod
    def listar_empleados(cls) -> list:
        with Conexion():
            Conexion.crear_consulta(cls._SELECCIONAR)

        log.debug("Respuesta: " + str(Conexion.respuesta))
        empleados = Conexion.respuesta
        empleados = [Empleado(id=empleado[0], *empleado[1:]) for empleado in empleados]
        return empleados

    @classmethod
    def insertar_empleado(cls, empleado) -> int:
        with Conexion():
            Conexion.crear_consulta(
                cls._INSERTAR,
                empleado.nombre,
                empleado.apellido,
                empleado.edad,
                empleado.salario,
            )

        log.debug(f"Empleado {empleado.nombre} insertado")
        return Conexion.respuesta

    @classmethod
    def actualizar_empleado(cls, empleado):
        with Conexion():
            Conexion.crear_consulta(
                cls._ACTUALIZAR,
                empleado.nombre,
                empleado.apellido,
                empleado.edad,
                empleado.salario,
                empleado.id,
            )

        log.debug(f"Empleado {empleado.nombre} actualizado")
        return Conexion.respuesta

    @classmethod
    def eliminar_empleado(cls, empleado):
        with Conexion():
            Conexion.crear_consulta(cls._ELIMINAR, empleado.id)
            id_eliminado = Conexion.enviar_consulta()
            log.debug(f"Empleado {empleado.nombre} eliminado")
            return id_eliminado
