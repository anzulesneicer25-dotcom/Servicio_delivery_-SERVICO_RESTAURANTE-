from datos.conexion import Conexion
from dominio.factura import Factura


class FacturaDAO:
    @classmethod
    def insertar(cls, factura):
        conn = Conexion.obtenerConexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO factura (fecha, total, id_servicio) VALUES (?, ?, ?)",
            (factura.fecha, factura.total, factura.id_servicio)
        )
        conn.commit()

    @classmethod
    def buscar(cls, id_factura):
        conn = Conexion.obtenerConexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM factura WHERE id_factura=?", (id_factura,))
        return cursor.fetchone()

    @classmethod
    def actualizar(cls, factura):
        conn = Conexion.obtenerConexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE factura
            SET fecha=?, total=?, id_servicio=?
            WHERE id_factura=?
        """, (factura.fecha, factura.total, factura.id_servicio, factura.id_factura))
        conn.commit()

    @classmethod
    def eliminar(cls, id_factura):
        conn = Conexion.obtenerConexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM factura WHERE id_factura=?", (id_factura,))
        conn.commit()
