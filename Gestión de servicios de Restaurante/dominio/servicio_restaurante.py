#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE
class ServicioRestaurante:
    '''
    Clase base que representa un servicio de restaurante.
    '''
    def __init__(self, id_servicio: str, cliente: str, costo_base):
        self.id_servicio = id_servicio
        self.cliente = cliente
        self.costo_base = float(costo_base)  # conversión obligatoria a float

    @property
    def id_servicio(self):
        return self._id_servicio

    @id_servicio.setter
    def id_servicio(self, valor):
        if not valor.strip():
            raise ValueError("El ID del servicio no puede estar vacío.")
        self._id_servicio = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if not valor.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")
        self._cliente = valor

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor):
        try:
            valor = float(valor)
        except Exception:
            raise ValueError("El costo base debe ser un número.")
        if valor < 0:
            raise ValueError("El costo base no puede ser negativo.")
        self._costo_base = valor

    def __str__(self):
        return (f"ServicioRestaurante[ ID: {self._id_servicio}, "
                f"Cliente: {self._cliente}, "
                f"Costo base: {self._costo_base} ]")


