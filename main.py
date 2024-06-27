from dominio.Empleado import Empleado
from servicio.Conexion import Conexion
from interfaz.EmpleadoDAO import EmpleadoDAO
from logcon import log
from servicio.Menu import Menu


def main():
    log.info("Inicio del programa")
    print("\n", "Bienvenido al sistema de empleados".center(60, "="), "\n")
    opcion_usuario = ""
    while opcion_usuario != "5":
        opcion_usuario = input(
            "\n1. Listar Empleados\n2. Agregar Empleado\n3. Buscar por ID\n4. Eliminar por ID\n5. Salir\n"
        )
        log.info(f"Opcion seleccionada: {opcion_usuario}")
        if opcion_usuario.strip() == "1":
            Menu.listar()
            input("Presione enter para continuar")
    # empleado = Empleado("Juan", "Perez", 22, 1000, id=1)
    # EmpleadoDAO.insertar_empleado(empleado)
    # for empleado in EmpleadoDAO.listar_empleados():
    #     log.debug(empleado)
    # print(EmpleadoDAO.eliminar_empleado(empleado))

    # EmpleadoDAO.actualizar_empleado(empleado)
    print("\n", "Fin del programa".center(60, "="), "\n")
    log.debug("Fin del programa")


if __name__ == "__main__":
    main()
