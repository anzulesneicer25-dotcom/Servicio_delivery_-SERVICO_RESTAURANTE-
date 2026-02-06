# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'servicio_delivery.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_Serviciodelivery(object):
    def setupUi(self, Serviciodelivery):
        if not Serviciodelivery.objectName():
            Serviciodelivery.setObjectName(u"Serviciodelivery")
        Serviciodelivery.resize(756, 525)
        self.centralwidget = QWidget(Serviciodelivery)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblID_servicio = QLabel(self.centralwidget)
        self.lblID_servicio.setObjectName(u"lblID_servicio")
        self.lblID_servicio.setGeometry(QRect(50, 50, 151, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblID_servicio.setFont(font)
        self.txtID_servicio = QLineEdit(self.centralwidget)
        self.txtID_servicio.setObjectName(u"txtID_servicio")
        self.txtID_servicio.setGeometry(QRect(200, 50, 381, 41))
        self.txtID_servicio.setMaxLength(25)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(40, 390, 121, 61))
        self.btnGuardar.setFont(font)
        self.txtcliente = QLineEdit(self.centralwidget)
        self.txtcliente.setObjectName(u"txtcliente")
        self.txtcliente.setGeometry(QRect(200, 110, 381, 41))
        self.txtcliente.setMaxLength(25)
        self.lblcliente = QLabel(self.centralwidget)
        self.lblcliente.setObjectName(u"lblcliente")
        self.lblcliente.setGeometry(QRect(100, 110, 151, 51))
        self.lblcliente.setFont(font)
        self.txtcosto_base = QLineEdit(self.centralwidget)
        self.txtcosto_base.setObjectName(u"txtcosto_base")
        self.txtcosto_base.setGeometry(QRect(200, 230, 381, 41))
        self.txtcosto_base.setMaxLength(25)
        self.lblcosto_base = QLabel(self.centralwidget)
        self.lblcosto_base.setObjectName(u"lblcosto_base")
        self.lblcosto_base.setGeometry(QRect(50, 220, 151, 51))
        self.lblcosto_base.setFont(font)
        self.txtdireccion = QLineEdit(self.centralwidget)
        self.txtdireccion.setObjectName(u"txtdireccion")
        self.txtdireccion.setGeometry(QRect(200, 170, 381, 41))
        self.txtdireccion.setMaxLength(25)
        self.lbldireccion = QLabel(self.centralwidget)
        self.lbldireccion.setObjectName(u"lbldireccion")
        self.lbldireccion.setGeometry(QRect(70, 160, 151, 51))
        self.lbldireccion.setFont(font)
        self.lbltarifa = QLabel(self.centralwidget)
        self.lbltarifa.setObjectName(u"lbltarifa")
        self.lbltarifa.setGeometry(QRect(10, 270, 191, 51))
        self.lbltarifa.setFont(font)
        self.txttarifa = QLineEdit(self.centralwidget)
        self.txttarifa.setObjectName(u"txttarifa")
        self.txttarifa.setGeometry(QRect(200, 280, 381, 41))
        self.txttarifa.setMaxLength(25)
        self.btnBuscar = QPushButton(self.centralwidget)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(590, 40, 121, 61))
        self.btnBuscar.setFont(font)
        self.btnActualizar = QPushButton(self.centralwidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(180, 390, 131, 61))
        self.btnActualizar.setFont(font)
        self.btnEliminar = QPushButton(self.centralwidget)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(320, 390, 121, 61))
        self.btnEliminar.setFont(font)
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(450, 390, 121, 61))
        self.btnLimpiar.setFont(font)
        self.lbltotal = QLabel(self.centralwidget)
        self.lbltotal.setObjectName(u"lbltotal")
        self.lbltotal.setGeometry(QRect(50, 330, 151, 51))
        self.lbltotal.setFont(font)
        Serviciodelivery.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Serviciodelivery)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 756, 31))
        Serviciodelivery.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Serviciodelivery)
        self.statusbar.setObjectName(u"statusbar")
        Serviciodelivery.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtID_servicio, self.txtcliente)
        QWidget.setTabOrder(self.txtcliente, self.txtdireccion)
        QWidget.setTabOrder(self.txtdireccion, self.txtcosto_base)
        QWidget.setTabOrder(self.txtcosto_base, self.txttarifa)
        QWidget.setTabOrder(self.txttarifa, self.btnBuscar)
        QWidget.setTabOrder(self.btnBuscar, self.btnGuardar)
        QWidget.setTabOrder(self.btnGuardar, self.btnActualizar)
        QWidget.setTabOrder(self.btnActualizar, self.btnEliminar)
        QWidget.setTabOrder(self.btnEliminar, self.btnLimpiar)

        self.retranslateUi(Serviciodelivery)

        QMetaObject.connectSlotsByName(Serviciodelivery)
    # setupUi

    def retranslateUi(self, Serviciodelivery):
        Serviciodelivery.setWindowTitle(QCoreApplication.translate("Serviciodelivery", u"Servico Delivery", None))
        self.lblID_servicio.setText(QCoreApplication.translate("Serviciodelivery", u"ID servicio :", None))
        self.btnGuardar.setText(QCoreApplication.translate("Serviciodelivery", u"Guardar", None))
        self.lblcliente.setText(QCoreApplication.translate("Serviciodelivery", u"Cliente:", None))
        self.txtcosto_base.setText("")
        self.lblcosto_base.setText(QCoreApplication.translate("Serviciodelivery", u"Costo base :", None))
        self.txtdireccion.setText("")
        self.lbldireccion.setText(QCoreApplication.translate("Serviciodelivery", u"Direcci\u00f3n:", None))
        self.lbltarifa.setText(QCoreApplication.translate("Serviciodelivery", u"Tarifa de Env\u00edo:", None))
        self.txttarifa.setText("")
        self.btnBuscar.setText(QCoreApplication.translate("Serviciodelivery", u"Buscar", None))
        self.btnActualizar.setText(QCoreApplication.translate("Serviciodelivery", u"Actualizar", None))
        self.btnEliminar.setText(QCoreApplication.translate("Serviciodelivery", u"Eliminar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("Serviciodelivery", u"Limpiar ", None))
        self.lbltotal.setText(QCoreApplication.translate("Serviciodelivery", u"Total:", None))
    # retranslateUi

