#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ANZULES AGUILAR NEICER JOSUE
# MOREIRA AGUIÑO JARIB JORGE
import sys
from PySide6.QtWidgets import QApplication
from servicio.ventana_delivery import VentanaDelivery

app = QApplication(sys.argv)
ventana = VentanaDelivery()
ventana.show()
sys.exit(app.exec())