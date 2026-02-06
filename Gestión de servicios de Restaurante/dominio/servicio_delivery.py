#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ANZULES AGUILAR NEICER JOSUE
# MOREIRA AGUIÑO JARIB JORGE
from dominio.servicio_restaurante import ServicioRestaurante

class ServicioDelivery(ServicioRestaurante):
    """
    Clase que representa un servicio de entrega a domicilio.
    Hereda de ServicioRestaurante.
    """

    def __init__(self, id_servicio, cliente, costo_base, direccion, tarifa_envio, fecha_registro=None):
        super().__init__(id_servicio, cliente, float(costo_base))
        self.direccion = direccion
        self.tarifa_envio = tarifa_envio
        self.fecha_registro = fecha_registro

    # ---------- Dirección ----------
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
        if not valor.strip():
            raise ValueError("La dirección no puede estar vacía.")
        self._direccion = valor

    # ---------- Tarifa de envío ----------
    @property
    def tarifa_envio(self):
        return self._tarifa_envio

    @tarifa_envio.setter
    def tarifa_envio(self, valor):
        try:
            valor = float(valor)
        except Exception:
            raise ValueError("La tarifa de envío debe ser un número.")
        if valor < 0:
            raise ValueError("La tarifa de envío no puede ser negativa.")
        self._tarifa_envio = valor

    # ---------- Métodos de negocio ----------
    def calcular(self):
        """Calcula el total sumando costo base + tarifa de envío."""
        return float(self.costo_base) + float(self.tarifa_envio)

    def mostrar_info(self):
        return (f"[Delivery] ID:{self.id_servicio} - Cliente:{self.cliente} "
                f"- Dirección:{self.direccion} - Total:${self.calcular():.2f}")

    def __str__(self):
        return (f"ServicioDelivery[ ID: {self.id_servicio}, "
                f"Cliente: {self.cliente}, "
                f"Dirección: {self.direccion}, "
                f"Tarifa envío: {self.tarifa_envio:.2f}, "
                f"Total: {self.calcular():.2f} ]")