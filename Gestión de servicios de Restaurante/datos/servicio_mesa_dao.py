from datos.conexion import Conexion
from dominio.servicio_mesa import ServicioMesa


class ServicioMesaDAO:
    @classmethod
    def insertar(cls, servicio: ServicioMesa):
        cursor = Conexion.obtenerCursor()
        cursor.execute("INSERT INTO servicio_mesa VALUES (?, ?, ?, ?, ?)",
                       (servicio.id_servicio, servicio.cliente, servicio.costo_base,
                        servicio.numero_mesa, servicio.propina))
        Conexion.obtenerConexion().commit()

    @classmethod
    def buscar(cls, id_servicio: str):
        cursor = Conexion.obtenerCursor()
        cursor.execute("SELECT * FROM servicio_mesa WHERE id_servicio=?", (id_servicio,))
        return cursor.fetchone()

    @classmethod
    def actualizar(cls, servicio: ServicioMesa):
        cursor = Conexion.obtenerCursor()
        cursor.execute("""
            UPDATE servicio_mesa SET cliente=?, costo_base=?, numero_mesa=?, propina=? WHERE id_servicio=?
        """, (servicio.cliente, servicio.costo_base, servicio.numero_mesa, servicio.propina, servicio.id_servicio))
        Conexion.obtenerConexion().commit()

    @classmethod
    def eliminar(cls, id_servicio: str):
        cursor = Conexion.obtenerCursor()
        cursor.execute("DELETE FROM servicio_mesa WHERE id_servicio=?", (id_servicio,))
        Conexion.obtenerConexion().commit()
