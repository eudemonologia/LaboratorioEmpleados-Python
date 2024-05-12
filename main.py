from dominio.Empleado import Empleado
from servicio.Conexion import Conexion
from interfaz.EmpleadoDAO import EmpleadoDAO
from logcon import log


def main():
    log.debug("Inicio del programa")
    empleado = Empleado("Juan", "Perez", 22, 1000, id=1)
    EmpleadoDAO.insertar_empleado(empleado)
    # for empleado in EmpleadoDAO.listar_empleados():
    #     log.debug(empleado)
    # print(EmpleadoDAO.eliminar_empleado(empleado))

    # EmpleadoDAO.actualizar_empleado(empleado)
    log.debug("Fin del programa")


if __name__ == "__main__":
    main()
