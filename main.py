from servicio.Conexion import Conexion
from logcon import log
from servicio.Menu import Menu


def main():
    log.info("Inicio del programa")
    print("\n", "Bienvenido al sistema de empleados".center(60, "="), "\n")
    opcion_usuario = ""

    Conexion.crear_bd()

    while opcion_usuario != "6":
        opcion_usuario = input(
            "\n1. Listar Empleados\n2. Agregar Empleado\n3. Buscar por ID\n4. Actualizar por ID\n5. Eliminar por ID\n6. Salir\n"
        )
        log.info(f"Opcion seleccionada: {opcion_usuario}")

        if opcion_usuario.strip() == "1":
            Menu.listar()
            input("Presione enter para continuar")

        elif opcion_usuario.strip() == "2":
            Menu.agregar()
            input("Presione enter para continuar")

        elif opcion_usuario.strip() == "3":
            Menu.buscar(input("Ingrese el ID del empleado: ").strip())
            input("Presione enter para continuar")

        elif opcion_usuario.strip() == "4":
            Menu.actualizar(input("Ingrese el ID del empleado: ").strip())
            input("Presione enter para continuar")

        elif opcion_usuario.strip() == "5":
            Menu.eliminar(input("Ingrese el ID del empleado: ").strip())
            input("Presione enter para continuar")

        else:
            print("Opcion no valida")

    print("\n", "Fin del programa".center(60, "="), "\n")
    log.debug("Fin del programa")


if __name__ == "__main__":
    main()
