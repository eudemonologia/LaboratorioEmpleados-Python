# Clase Conexion que permite la conexión a la base de datos

import sqlite3
from logcon import log


class Conexion:
    # Nombre del archivo
    _DATABASE = "db.sqlite"

    _conexion = None
    _cursor = None
    _consulta = None
    respuesta = None

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = sqlite3.connect(cls._DATABASE)
                log.debug("Se abrió correctamente la conexión a la base de datos.")
            except sqlite3.Error as e:
                log.error("Error al conectar a la base de datos: " + str(e))
        else:
            log.debug("Conexión ya estaba creada")

    @classmethod
    def obtener_cursor(cls):
        if cls._conexion is not None:
            if cls._cursor is None:
                try:
                    cls._cursor = cls._conexion.cursor()
                    log.debug("Se abrió correctamente el cursor.")
                    return cls._cursor
                except sqlite3.Error as e:
                    log.error("Error al conectar a la base de datos: " + str(e))
            else:
                log.debug("Cursor ya estaba creado")
                return cls._cursor
        else:
            log.error("No se ha establecido una conexión a la base de datos.")

    @classmethod
    def crear_consulta(cls, consulta, *args):
        if cls._consulta is None:
            try:
                cls._consulta = cls._cursor.execute(consulta, args)
                log.debug("Consulta ejecutada correctamente.")
                print(cls._consulta)
            except sqlite3.Error as e:
                cls._conexion.rollback()
                log.error("Error al ejecutar la consulta: " + str(e))
        else:
            log.debug("Consulta ya estaba creada")

    @classmethod
    def cerrar_cursor(cls):
        if cls._cursor is not None:
            try:
                cls._cursor.close()
                cls._cursor = None
                log.debug("Se cerró correctamente el cursor.")
            except sqlite3.Error as e:
                log.error("Error al cerrar el cursor: " + str(e))
        else:
            log.debug("Cursor ya estaba cerrado")

    @classmethod
    def cerrar_conexion(cls):
        if cls._conexion is not None:
            cls._conexion.close()
            cls._conexion = None
            log.debug("Se cerró correctamente la conexión a la base de datos")
        else:
            log.debug("Conexion ya cerrada")

    @classmethod
    def crear_bd(cls):
        cls.obtener_conexion()
        cls.obtener_cursor()
        cls.enviar_consulta(
            """
            CREATE TABLE IF NOT EXISTS empleados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                edad INTEGER NOT NULL,
                salario REAL NOT NULL
            )                         
            """
        )
        cls.cerrar_cursor()
        cls.cerrar_conexion()
        log.debug("Se creó correctamente la base de datos.")

    def __enter__(self):
        Conexion.obtener_conexion()
        Conexion.obtener_cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            Conexion._conexion.rollback()
            log.error(f"Error al enviar la consulta: {exc_type} - {exc_val} - {exc_tb}")
            Conexion.cerrar_cursor()
            Conexion.cerrar_conexion()
        else:
            Conexion._conexion.commit()
            log.debug("Consulta enviada correctamente.")

            Conexion.respuesta = (
                Conexion._cursor.fetchall() or Conexion._cursor.rowcount
            )
            log.debug(f"Respuesta: {Conexion.respuesta}")
            Conexion.cerrar_cursor()
            Conexion.cerrar_conexion()
