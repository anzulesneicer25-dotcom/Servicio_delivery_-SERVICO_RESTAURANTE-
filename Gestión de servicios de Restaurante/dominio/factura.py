#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE
class Factura:
    '''
    Clase que representa una factura de un servicio.
    Puede generarse desde un objeto ServicioDelivery o desde la BD.
    '''
    def __init__(self, id_factura=None, fecha=None, total=None, id_servicio=None, servicio=None):
        self.id_factura = id_factura
        self.fecha = fecha
        self.id_servicio = id_servicio
        self.servicio = servicio

        # Si se pasa un servicio, calculamos el total
        if servicio is not None:
            self.total = servicio.costo_base + servicio.tarifa_envio
        else:
            self.total = total

    def generar_factura(self):
        print("=== FACTURA ===")
        print("ID:", self.id_factura if self.id_factura else "Pendiente")
        print("Fecha:", self.fecha)
        if self.servicio:
            print("Cliente:", self.servicio.cliente)
            print("Dirección:", self.servicio.direccion)
            print("Costo Base:", self.servicio.costo_base)
            print("Tarifa Envío:", self.servicio.tarifa_envio)
        print("Total a pagar:", self.total)

    def __str__(self):
        return f"Factura del {self.fecha} - Total: ${self.total:.2f}"

