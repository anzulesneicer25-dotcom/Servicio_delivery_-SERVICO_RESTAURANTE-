from datos.conexion import Conexion
from dominio.empleado import Empleado


class EmpleadoDAO:
    @classmethod
    def insertar(cls, empleado: Empleado):
        cursor = Conexion.obtenerCursor()
        cursor.execute("INSERT INTO empleados (nombre, cargo) VALUES (?, ?)",
                       (empleado.nombre, empleado.cargo))
        Conexion.obtenerConexion().commit()

    @classmethod
    def buscar(cls, nombre: str):
        cursor = Conexion.obtenerCursor()
        cursor.execute("SELECT * FROM empleados WHERE nombre=?", (nombre,))
        return cursor.fetchone()

    @classmethod
    def actualizar(cls, id_empleado: int, empleado: Empleado):
        cursor = Conexion.obtenerCursor()
        cursor.execute("""
            UPDATE empleados SET nombre=?, cargo=? WHERE id_empleado=?
        """, (empleado.nombre, empleado.cargo, id_empleado))
        Conexion.obtenerConexion().commit()

    @classmethod
    def eliminar(cls, id_empleado: int):
        cursor = Conexion.obtenerCursor()
        cursor.execute("DELETE FROM empleados WHERE id_empleado=?", (id_empleado,))
        Conexion.obtenerConexion().commit()
