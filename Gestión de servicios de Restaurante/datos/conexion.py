import sys
import pyodbc

class Conexion:
    _SERVIDOR = '127.0.0.1'
    _BBDD = 'SAP'
    _USUARIO = 'GSR'
    _PASSWORD = '1234'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=localhost;'
                    'DATABASE=SAP;'
                    'UID=GSR;'
                    'PWD=1234;'
                    'TrustServerCertificate=yes'
                )

                return cls._conexion
            except Exception as e:
                print("Error al conectar:", e)
                sys.exit()
        return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                return cls._cursor
            except Exception as e:
                print("Error al abrir cursor:", e)
                sys.exit()
        return cls._cursor
