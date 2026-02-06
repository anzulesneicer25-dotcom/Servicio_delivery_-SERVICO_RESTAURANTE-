#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ANZULES AGUILAR NEICER JOSUE
# MOREIRA AGUIÑO JARIB JORGE
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QDoubleValidator
from ui.servicio_delivery_ui import Ui_Serviciodelivery
from dominio.servicio_delivery import ServicioDelivery
from datos.servicio_delivery_dao import ServicioDeliveryDAO
from datetime import date


class VentanaDelivery(QMainWindow):
    '''
    Clase que genera la lógica de los objetos de ServicioDelivery
    '''
    def __init__(self):
        super().__init__()
        self.ui = Ui_Serviciodelivery()
        self.ui.setupUi(self)

        # Conectar botones
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)

        # Conectar cálculo automático del total
        self.ui.txtcosto_base.textChanged.connect(self.calcular_total)
        self.ui.txttarifa.textChanged.connect(self.calcular_total)

        # Validadores para campos numéricos
        self.ui.txtcosto_base.setValidator(QDoubleValidator(0.0, 9999.99, 2))
        self.ui.txttarifa.setValidator(QDoubleValidator(0.0, 9999.99, 2))

    # ------------------ CALCULAR TOTAL ------------------
    def calcular_total(self):
        try:
            costo_texto = self.ui.txtcosto_base.text().strip()
            tarifa_texto = self.ui.txttarifa.text().strip()

            if costo_texto and tarifa_texto:  # Solo si ambos tienen valor
                costo = float(costo_texto)
                tarifa = float(tarifa_texto)
                total = costo + tarifa
                self.ui.lbltotal.setText(f"Total: ${total:.2f}")
            else:
                self.ui.lbltotal.setText("Total: -")
        except Exception:
            self.ui.lbltotal.setText("Total: -")

    # ------------------ GUARDAR ------------------
    def guardar(self):
        id_servicio = self.ui.txtID_servicio.text().strip()
        cliente = self.ui.txtcliente.text().strip()
        costo_base = self.ui.txtcosto_base.text().strip()
        direccion = self.ui.txtdireccion.text().strip()
        tarifa = self.ui.txttarifa.text().strip()
        fecha_registro = date.today()

        # Validaciones una por una
        if id_servicio == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un ID de servicio")
            return
        elif cliente == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el nombre del cliente")
            return
        elif not cliente.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "El nombre del cliente debe contener solo letras")
            return
        elif costo_base == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un costo base")
            return
        elif direccion == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una dirección")
            return
        elif tarifa == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una tarifa")
            return
        try:
            float(costo_base)
            float(tarifa)
        except ValueError:
            QMessageBox.warning(self, "Advertencia", "Costo base y tarifa deben ser números válidos")
            return

        # Si todo está correcto, se guarda
        try:
            servicio = ServicioDelivery(id_servicio, cliente, float(costo_base), direccion, float(tarifa), fecha_registro)
            respuesta = ServicioDeliveryDAO.insertar(servicio)
            if respuesta["ejecuto"]:
                self.ui.statusbar.showMessage("Servicio guardado con éxito", 1500)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", respuesta["mensaje"])
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ------------------ BUSCAR ------------------
    def buscar(self):
        id_servicio = self.ui.txtID_servicio.text().strip()
        if id_servicio == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un ID de servicio")
            return

        servicio = ServicioDeliveryDAO.buscar(id_servicio)
        if servicio:
            self.ui.txtcliente.setText(servicio.cliente)
            self.ui.txtcosto_base.setText(str(servicio.costo_base))
            self.ui.txtdireccion.setText(servicio.direccion)
            self.ui.txttarifa.setText(str(servicio.tarifa_envio))
            self.calcular_total()
        else:
            QMessageBox.warning(self, "Advertencia", "No existe servicio registrado con ese ID")

    # ------------------ ACTUALIZAR ------------------
    def actualizar(self):
        id_servicio = self.ui.txtID_servicio.text().strip()
        cliente = self.ui.txtcliente.text().strip()
        costo_base = self.ui.txtcosto_base.text().strip()
        direccion = self.ui.txtdireccion.text().strip()
        tarifa = self.ui.txttarifa.text().strip()

        # Validaciones una por una
        if id_servicio == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un ID de servicio")
            return
        elif cliente == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el nombre del cliente")
            return
        elif not cliente.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "El nombre del cliente debe contener solo letras")
            return
        elif costo_base == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un costo base")
            return
        elif direccion == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una dirección")
            return
        elif tarifa == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una tarifa")
            return
        try:
            float(costo_base)
            float(tarifa)
        except ValueError:
            QMessageBox.warning(self, "Advertencia", "Costo base y tarifa deben ser números válidos")
            return

        # Si todo está correcto, se actualiza
        try:
            servicio = ServicioDelivery(id_servicio, cliente, float(costo_base), direccion, float(tarifa))
            respuesta = ServicioDeliveryDAO.actualizar(servicio)
            if respuesta["ejecuto"]:
                self.ui.statusbar.showMessage("Servicio actualizado con éxito", 1500)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", respuesta["mensaje"])
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ------------------ ELIMINAR ------------------
    def eliminar(self):
        id_servicio = self.ui.txtID_servicio.text().strip()
        if id_servicio == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un ID de servicio")
            return

        if QMessageBox.question(self, "Confirmación", "¿Está seguro de eliminar este servicio?") == QMessageBox.Yes:
            try:
                respuesta = ServicioDeliveryDAO.eliminar_por_id(id_servicio)
                if respuesta["ejecuto"]:
                    self.ui.statusbar.showMessage("Servicio eliminado con éxito", 1500)
                    self.limpiar()
                else:
                    QMessageBox.critical(self, "Error", respuesta["mensaje"])
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            print("Acción cancelada por el usuario")

    # ------------------ LIMPIAR ------------------
    def limpiar(self):
        self.ui.txtID_servicio.clear()
        self.ui.txtcliente.clear()
        self.ui.txtcosto_base.clear()
        self.ui.txtdireccion.clear()
        self.ui.txttarifa.clear()
        self.ui.lbltotal.setText("Total: -")