#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE
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
