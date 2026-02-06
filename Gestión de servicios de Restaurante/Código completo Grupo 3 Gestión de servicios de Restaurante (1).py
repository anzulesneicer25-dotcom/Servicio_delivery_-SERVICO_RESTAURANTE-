#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE

class ServicioRestaurante:
    """
    Superclase base para todos los servicios del restaurante.
    """

    def __init__(self, id_servicio: str, cliente: str, costo_base: float):
        self.id_servicio = id_servicio
        self.cliente = cliente
        self.costo_base = costo_base

    @property
    def id_servicio(self):
        return self._id_servicio

    @id_servicio.setter
    def id_servicio(self, valor):
        if valor.strip() == "":
            raise ValueError("El ID del servicio no puede estar vacío.")
        self._id_servicio = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre del cliente no puede estar vacío.")
        self._cliente = valor

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor):
        if valor < 0:
            raise ValueError("El costo base no puede ser negativo.")
        self._costo_base = valor

    # ======= MÉTODO BASE POLIMÓRFICO =======
    def calcular(self):
        return self.costo_base
    # ======= MÉTODO BASE DE INFORMACIÓN =======
    def mostrar_info(self):
        return f"Servicio {self.id_servicio} para {self.cliente} - Costo base: {self.costo_base}"
if __name__ == '__main__':
    print("=== PRUEBA DE SERVICIO RESTAURANTE ===")

    try:
        # Crear un servicio válido
        servicio1 = ServicioRestaurante("SR001", "Juan Pérez", 15.50)
        print("Servicio creado correctamente:")
        print("ID:", servicio1.id_servicio)
        print("Cliente:", servicio1.cliente)
        print("Costo base:", servicio1.costo_base)

        # Intentar crear un servicio con costo negativo
        print("\nIntentando crear servicio con costo negativo...")
        servicio2 = ServicioRestaurante("SR002", "Ana", -10)

    except Exception as e:
        print("Error detectado:", e)

    try:
        # Intentar crear un servicio con cliente vacío
        print("\nIntentando crear servicio con cliente vacío...")
        servicio3 = ServicioRestaurante("SR003", "", 20)  # debe fallar

    except Exception as e:
        print("Error detectado:", e)
from dominio.servicio_restaurante import ServicioRestaurante
class ServicioMesa(ServicioRestaurante):
    '''
    Clase que representa un servicio en mesa dentro del restaurante.
    Hereda de ServicioRestaurante.
    '''
    def __init__(self, id_servicio: str, cliente: str, costo_base: float, numero_mesa: int, propina: float):
        ServicioRestaurante.__init__(self, id_servicio, cliente, costo_base)
        self.numero_mesa = numero_mesa
        self.propina = propina

    @property
    def numero_mesa(self):
        return self._numero_mesa

    @numero_mesa.setter
    def numero_mesa(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El número de mesa debe ser un entero mayor que 0.")
        self._numero_mesa = valor

    @property
    def propina(self):
        return self._propina

    @propina.setter
    def propina(self, valor):
        try:
            valor = float(valor)
        except:
            raise ValueError("La propina debe ser un número.")

        if valor < 0:
            raise ValueError("La propina no puede ser negativa.")

        self._propina = valor

    def calcular(self):
        '''Calcula el total sumando costo base + propina'''
        return self.costo_base + self.propina

    def mostrar_info(self):
        '''Muestra la información del servicio de mesa'''
        return (f"[Servicio Mesa] ID:{self.id_servicio} - Cliente:{self.cliente} "
                f"- Mesa:{self.numero_mesa} - Total:${self.calcular():.2f}")
if __name__ == '__main__':
    print("=== PRUEBA DE SERVICIO MESA ===")

    try:
        mesa1 = ServicioMesa("M001", "Carlos", 20.0, 5, 3.5)
        print(mesa1.mostrar_info())

        # Prueba: mesa inválida
        print("\nIntentando crear servicio con mesa inválida...")
        mesa2 = ServicioMesa("M002", "Ana", 15.0, -1, 2.0)

    except Exception as e:
        print("Error detectado:", e)

    try:
        # Prueba: propina negativa
        print("\nIntentando crear servicio con propina negativa...")
        mesa3 = ServicioMesa("M003", "Luis", 12.0, 3, -5)

    except Exception as e:
        print("Error detectado:", e)

    print("\n=== FIN DE LA PRUEBA ===")
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

from dominio.servicio_restaurante import ServicioRestaurante


class ServicioDelivery(ServicioRestaurante):
    '''
          Clase que representa un servicio de entrega a domicilio.
          Hereda de ServicioRestaurante.
    '''
    def __init__(self, id_servicio: str, cliente: str, costo_base: float,
                 direccion: str, tarifa_envio: float):
        ServicioRestaurante.__init__(self,id_servicio,cliente,costo_base)
        self.direccion = direccion
        self.tarifa_envio = tarifa_envio

        @property
        def direccion(self):
            return self._direccion

        @direccion.setter
        def direccion(self, valor):
            if valor.strip() == "":
                raise ValueError("La dirección no puede estar vacía.")
            self._direccion = valor

        @property
        def tarifa_envio(self):
            return self._tarifa_envio

        @tarifa_envio.setter
        def tarifa_envio(self, valor):
            try:
                valor = float(valor)
            except:
                raise ValueError("La tarifa de envío debe ser un número.")

            if valor < 0:
                raise ValueError("La tarifa de envío no puede ser negativa.")

            self._tarifa_envio = valor
# Métodos polimórficos
    # ================================

    def calcular(self):
        '''Calcula el total sumando costo base + tarifa de envío'''
        return self.costo_base + self.tarifa_envio

    def mostrar_info(self):
        '''Muestra la información del servicio delivery'''
        return (f"[Delivery] ID:{self.id_servicio} - Cliente:{self.cliente} "
                f"- Dirección:{self.direccion} - Total:${self.calcular():.2f}")

if __name__ == '__main__':
    print("=== PRUEBA DE SERVICIO DELIVERY ===")

    try:
        delivery1 = ServicioDelivery("D001", "María López", 18.0,
                                     "Calle Principal 123", 2.5)
        print(delivery1.mostrar_info())

        # Prueba: dirección vacía
        print("\nIntentando crear delivery con dirección vacía...")
        delivery2 = ServicioDelivery("D002", "Carlos", 12.0, "", 3.0)

    except Exception as e:
        print("Error detectado:", e)

    try:
        # Prueba: tarifa negativa
        print("\nIntentando crear delivery con tarifa negativa...")
        delivery3 = ServicioDelivery("D003", "Ana", 10.0, "Av. Quito", -1.5)

    except Exception as e:
        print("Error detectado:", e)

    print("\n=== FIN DE LA PRUEBA ===")

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
class Empleado:
    '''
        Clase que representa un empleado del restaurante.
    '''
    def __init__(self, nombre: str, cargo: str):
        self.nombre = nombre
        self.cargo = cargo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre del empleado no puede estar vacío.")
        self._nombre = valor

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, valor):
        if valor.strip() == "":
            raise ValueError("El cargo no puede estar vacío.")
        self._cargo = valor
if __name__ == '__main__':
    print("=== PRUEBA DE CLASE EMPLEADO ===")

    # Crear empleados válidos
    empleado1 = Empleado("Carlos López", "Mesero")
    empleado2 = Empleado("Ana Torres", "Cajera")

    # Mostrar información
    print(f"Empleado 1: {empleado1.nombre} - Cargo: {empleado1.cargo}")
    print(f"Empleado 2: {empleado2.nombre} - Cargo: {empleado2.cargo}")

    # Probar setters (cambiar valores)
    empleado1.nombre = "Carlos L."
    empleado1.cargo = "Supervisor de Mesas"
    print("\nDespués de actualizar datos:")
    print(f"Empleado 1: {empleado1.nombre} - Cargo: {empleado1.cargo}")

    # Probar validaciones
    print("\n--- PRUEBAS DE VALIDACIONES ---")
    try:
        empleado_malo = Empleado("", "Cocinero")   # Nombre vacío
    except ValueError as e:
        print("Error al crear empleado:", e)

    try:
        empleado1.cargo = ""   # Cargo vacío
    except ValueError as e:
        print("Error al asignar cargo:", e)
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
class Factura:
    '''
        Clase que genera una factura del servicio.
    '''
    def __init__(self, servicio, fecha):
        self.servicio = servicio
        self.fecha = fecha

    def generar_factura(self):
        print("=== FACTURA ===")
        print("Fecha:", self.fecha)
        print("Servicio:", self.servicio.mostrar_info())
        print("Total a pagar:", self.servicio.calcular())

if __name__ == '__main__':
    print("=== PRUEBA DE CLASE FACTURA ===")


    # Creamos un servicio de ejemplo (puedes usar ServicioMesa o ServicioDelivery)
    class ServicioEjemplo:
        """Clase temporal solo para probar Factura."""

        def __init__(self):
            self._descripcion = "Servicio de prueba"

        def mostrar_info(self):
            return self._descripcion

        def calcular(self):
            return 25.50


    servicio = ServicioEjemplo()

    # Crear factura
    factura = Factura(servicio, "10/03/2025")

    # Generar factura
    factura.generar_factura()
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------


from dominio.servicio_restaurante import ServicioRestaurante
from dominio.servicio_mesa import ServicioMesa
from dominio.servicio_delivery import ServicioDelivery
from dominio.empleado import Empleado
from dominio.factura import Factura

if __name__ == '__main__':
    print("=== SISTEMA DE GESTIÓN DE SERVICIOS DE RESTAURANTE ===\n")

    print(">>> Demostrando uso de la SUPERCLASE ServicioRestaurante...\n")

    servicio_base = ServicioRestaurante("S000", "Cliente Base", 10.0)
    print("Servicio Base creado desde la superclase:")
    print(servicio_base.mostrar_info())
    print("Total calculado:", servicio_base.calcular(), "\n")

    # -------------------------------------------------------------
    # 1. Crear empleados
    # -------------------------------------------------------------
    print(">>> Creando empleados...")
    mesero = Empleado("Carlos López", "Mesero")
    repartidor = Empleado("Ana Torres", "Repartidora")

    print(f"Empleado creado: {mesero.nombre} - {mesero.cargo}")
    print(f"Empleado creado: {repartidor.nombre} - {repartidor.cargo}\n")

    # -------------------------------------------------------------
    # 2. Crear servicios (SUBCLASES)
    # -------------------------------------------------------------
    print(">>> Creando servicios...")

    servicio_mesa = ServicioMesa("S001", "Juan Pérez", 20.0, 3, 5.0)
    servicio_delivery = ServicioDelivery("S002", "María Gómez", 18.0, "Av. Central 123", 3.5)

    print("Servicios creados.\n")

    # -------------------------------------------------------------
    # 3. Lista polimórfica (NO SE PREGUNTA EL TIPO)
    # -------------------------------------------------------------
    print(">>> Lista polimórfica de servicios:")

    servicios = [servicio_mesa, servicio_delivery]

    for s in servicios:
        print("•", s.mostrar_info())
        print("  Total:", s.calcular())
        print()

    # -------------------------------------------------------------
    # 4. Crear Facturas
    # -------------------------------------------------------------
    print(">>> Generando facturas...\n")

    factura1 = Factura(servicio_mesa, "10/03/2025")
    factura2 = Factura(servicio_delivery, "10/03/2025")

    factura1.generar_factura()
    print()
    factura2.generar_factura()
    print()

    # -------------------------------------------------------------
    # 5. Polimorfismo real: sumar totales sin preguntar tipo
    # -------------------------------------------------------------
    print(">>> Calculando total general de ingresos del día...\n")

    total_general = sum(s.calcular() for s in servicios)

    print(f"Total recaudado con todos los servicios: ${total_general:.2f}")
    print("\n=== FIN DEL SISTEMA ===")
