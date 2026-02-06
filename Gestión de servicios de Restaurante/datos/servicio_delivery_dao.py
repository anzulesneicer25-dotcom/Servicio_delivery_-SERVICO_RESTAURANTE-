#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ANZULES AGUILAR NEICER JOSUE
# MOREIRA AGUIÑO JARIB JORGE
from datos.conexion import Conexion
from dominio.servicio_delivery import ServicioDelivery
import pyodbc as bd


class ServicioDeliveryDAO:
    _INSERT = ("INSERT INTO servicio_delivery (id_servicio, cliente, costo_base, direccion, tarifa_envio, fecha_registro) "
        "VALUES (?, ?, ?, ?, ?, ?)")

    _SELECT = ("SELECT id_servicio, cliente, costo_base, direccion, tarifa_envio "
        "FROM servicio_delivery WHERE id_servicio = ?")

    _UPDATE = ("UPDATE servicio_delivery SET cliente = ?, costo_base = ?, direccion = ?, tarifa_envio = ? "
        "WHERE id_servicio = ?")

    _DELETE = "DELETE FROM servicio_delivery WHERE id_servicio = ?"

    # ------------------ INSERTAR ------------------
    @classmethod
    def insertar(cls, servicio: ServicioDelivery):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (servicio.id_servicio,servicio.cliente,servicio.costo_base,servicio.direccion,servicio.tarifa_envio,
                    servicio.fecha_registro  )
                cursor.execute(cls._INSERT, datos)
                respuesta = cursor.rowcount
                if respuesta == 1:
                    return {"ejecuto": True, "mensaje": "Servicio guardado con éxito"}
                else:
                    return {"ejecuto": False, "mensaje": "No se insertó ningún registro"}
        except bd.IntegrityError as e_bb:
            print("Error en la inserción:", e_bb)
            return {"ejecuto": False, "mensaje": "Error de integridad"}
        except Exception as e:
            print("Error general:", e)
            return {"ejecuto": False, "mensaje": "Error al guardar los datos"}

    # ------------------ BUSCAR ------------------
    @classmethod
    def buscar(cls, id_servicio: str):
        servicio = None
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (id_servicio,)
                cursor.execute(cls._SELECT, datos)
                registro = cursor.fetchone()
                if registro:
                    servicio = ServicioDelivery(id_servicio=registro[0],cliente=registro[1],costo_base=registro[2],direccion=registro[3],tarifa_envio=registro[4])
                return servicio
        except Exception as e:
            print("Error general:", e)
            return None

    # ------------------ ACTUALIZAR ------------------
    @classmethod
    def actualizar(cls, servicio: ServicioDelivery):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (servicio.cliente,servicio.costo_base,servicio.direccion,servicio.tarifa_envio,servicio.id_servicio)
                cursor.execute(cls._UPDATE, datos)
                respuesta = cursor.rowcount
                if respuesta == 1:
                    return {"ejecuto": True, "mensaje": "Servicio actualizado con éxito"}
                else:
                    return {"ejecuto": False, "mensaje": "No se actualizó ningún registro"}
        except bd.IntegrityError as e_bb:
            print("Error en la actualización:", e_bb)
            return {"ejecuto": False, "mensaje": "Error de integridad"}
        except Exception as e:
            print("Error general:", e)
            return {"ejecuto": False, "mensaje": "Error al actualizar los datos"}

    # ------------------ ELIMINAR ------------------
    @classmethod
    def eliminar_por_id(cls, id_servicio: str):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (id_servicio,)
                cursor.execute(cls._DELETE, datos)
                respuesta = cursor.rowcount
                if respuesta == 1:
                    return {"ejecuto": True, "mensaje": "Servicio eliminado con éxito"}
                else:
                    return {"ejecuto": False, "mensaje": "No se eliminó ningún registro"}
        except Exception as e:
            print("Error general:", e)
            return {"ejecuto": False, "mensaje": "Error al eliminar servicio"}