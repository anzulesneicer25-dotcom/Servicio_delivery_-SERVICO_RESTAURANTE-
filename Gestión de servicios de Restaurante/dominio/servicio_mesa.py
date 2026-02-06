#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE
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
