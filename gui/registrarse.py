from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog
import datetime

from clases.validator import Validator

class Registrarse(QtWidgets.QWidget):
    def __init__(self, form, almacen_usuarios, parent=None):
        super().__init__(parent)
        self.almacen_usuarios = almacen_usuarios
        self.validador = Validator()
        self.form = form
        self.setupUi()

    def setupUi(self):
        self.form.setObjectName("self.form")
        self.form.resize(1102, 752)
        self.form.setMinimumSize(QtCore.QSize(1102, 752))
        self.form.setMaximumSize(QtCore.QSize(1102, 752))
        self.print_password = QtWidgets.QLabel(self.form)
        self.print_password.setGeometry(QtCore.QRect(130, 280, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_password.setFont(font)
        self.print_password.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_password.setText(str(QtCore.Qt.AutoText))
        self.print_password.setObjectName("print_password")
        self.print_confirm_password = QtWidgets.QLabel(self.form)
        self.print_confirm_password.setGeometry(QtCore.QRect(130, 390, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_confirm_password.setFont(font)
        self.print_confirm_password.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_confirm_password.setText(str(QtCore.Qt.AutoText))
        self.print_confirm_password.setObjectName("print_confirm_password")
        self.print_name = QtWidgets.QLabel(self.form)
        self.print_name.setGeometry(QtCore.QRect(470, 280, 81, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_name.setFont(font)
        self.print_name.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_name.setText(str(QtCore.Qt.AutoText))
        self.print_name.setObjectName("print_name")
        self.print_apellidos = QtWidgets.QLabel(self.form)
        self.print_apellidos.setGeometry(QtCore.QRect(470, 390, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_apellidos.setFont(font)
        self.print_apellidos.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_apellidos.setText(str(QtCore.Qt.AutoText))
        self.print_apellidos.setObjectName("print_apellidos")
        self.input_nickname = QtWidgets.QLineEdit(self.form)
        self.input_nickname.setGeometry(QtCore.QRect(130, 230, 291, 41))
        self.input_nickname.setObjectName("input_nickname")
        self.input_password = QtWidgets.QLineEdit(self.form)
        self.input_password.setGeometry(QtCore.QRect(130, 330, 291, 41))
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.input_gmail = QtWidgets.QLineEdit(self.form)
        self.input_gmail.setGeometry(QtCore.QRect(470, 230, 291, 41))
        self.input_gmail.setObjectName("input_gmail")
        self.input_confirm_password = QtWidgets.QLineEdit(self.form)
        self.input_confirm_password.setGeometry(QtCore.QRect(130, 440, 291, 41))
        self.input_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_confirm_password.setObjectName("input_confirm_password")
        self.input_nombre = QtWidgets.QLineEdit(self.form)
        self.input_nombre.setGeometry(QtCore.QRect(470, 330, 291, 41))
        self.input_nombre.setObjectName("input_nombre")
        self.foto_coche = QtWidgets.QLabel(self.form)
        self.foto_coche.setGeometry(QtCore.QRect(70, 450, 491, 351))
        self.foto_coche.setStyleSheet("image: url(:/fotos/logofast.png);")
        self.foto_coche.setText("")
        self.foto_coche.setObjectName("foto_coche")
        self.print_fecha_actual = QtWidgets.QLabel(self.form)
        self.print_fecha_actual.setGeometry(QtCore.QRect(890, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_fecha_actual.setFont(font)
        self.print_fecha_actual.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_fecha_actual.setText(str(QtCore.Qt.AutoText))
        self.print_fecha_actual.setObjectName("print_fecha_actual")
        self.print_nickname = QtWidgets.QLabel(self.form)
        self.print_nickname.setGeometry(QtCore.QRect(130, 170, 250, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_nickname.setFont(font)
        self.print_nickname.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_nickname.setText(str(QtCore.Qt.AutoText))
        self.print_nickname.setObjectName("print_nickname")
        self.boton_registrarse = QtWidgets.QPushButton(self.form)
        self.boton_registrarse.setGeometry(QtCore.QRect(780, 600, 231, 71))
        self.boton_registrarse.setStyleSheet("background-color: #09B5CB;\n"
"color: #FFFFFF;")
        self.boton_registrarse.setObjectName("boton_registrarse")
        self.boton_registrarse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.print_correo_electronico = QtWidgets.QLabel(self.form)
        self.print_correo_electronico.setGeometry(QtCore.QRect(470, 170, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_correo_electronico.setFont(font)
        self.print_correo_electronico.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_correo_electronico.setText(str(QtCore.Qt.AutoText))
        self.print_correo_electronico.setObjectName("print_correo_electronico")
        self.input_apellidos = QtWidgets.QLineEdit(self.form)
        self.input_apellidos.setGeometry(QtCore.QRect(470, 440, 291, 41))
        self.input_apellidos.setObjectName("input_apellidos")
        self.frame = QtWidgets.QFrame(self.form)
        self.frame.setGeometry(QtCore.QRect(-11, -21, 1181, 811))
        self.frame.setStyleSheet("\n"
"background-color: rgb(56, 56, 56);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.print_registrarse = QtWidgets.QLabel(self.frame)
        self.print_registrarse.setGeometry(QtCore.QRect(260, 40, 391, 131))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.print_registrarse.setFont(font)
        self.print_registrarse.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.print_registrarse.setMouseTracking(False)
        self.print_registrarse.setStyleSheet("font: 63 36pt \"Bahnschrift SemiBold\";\n"
"color: #09B5CB;\n"
"")
        self.print_registrarse.setObjectName("print_registrarse")
        self.frame.raise_()
        self.foto_coche.raise_()
        self.print_password.raise_()
        self.print_confirm_password.raise_()
        self.print_name.raise_()
        self.print_apellidos.raise_()
        self.input_nickname.raise_()
        self.input_password.raise_()
        self.input_gmail.raise_()
        self.input_confirm_password.raise_()
        self.input_nombre.raise_()
        self.print_fecha_actual.raise_()
        self.print_nickname.raise_()
        self.boton_registrarse.raise_()
        self.print_correo_electronico.raise_()
        self.input_apellidos.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.form)
        self.form.move(500, 120)
        self.form.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle(_translate("self.form", "Registrarse"))
        self.print_password.setText(_translate("self.form", "Contraseña"))
        self.print_confirm_password.setText(_translate("self.form", "Confirmar Contraseña"))
        self.print_name.setText(_translate("self.form", "Nombre"))
        self.print_apellidos.setText(_translate("self.form", "Apellidos"))
        fecha_actual = datetime.datetime.now().strftime("%H:%M:%S")
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_fecha)
        self.timer.start(1000) 
        self.print_fecha_actual.setText(_translate("self.form", fecha_actual))
        self.print_nickname.setText(_translate("self.form", "Nombre de Usuario"))
        self.boton_registrarse.setText(_translate("self.form", "REGISTRARSE"))
        self.print_correo_electronico.setText(_translate("self.form", "Correo Electrónico"))
        self.print_registrarse.setText(_translate("self.form", "REGISTRARSE"))

        self.boton_registrarse.clicked.connect(self.comprobar_registro)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.boton_registrarse.clicked.emit()
    
    def closeEvent(self, event):
        event.accept()
        self.volver_al_menu()

    def actualizar_fecha(self):
        fecha_actual = datetime.datetime.now().strftime("%H:%M:%S")
        self.print_fecha_actual.setText(fecha_actual)
     
    #COMPROBAR QUE LAS CONTRASEÑAS SEAN IGUALES
    def recoger_datos_registro(self):
        nickname_var = self.input_nickname.text()
        password_var = self.input_password.text()
        confirm_password_var = self.input_confirm_password.text()
        gmail_var = self.input_gmail.text()
        name_var = self.input_nombre.text()
        apellidos_var = self.input_apellidos.text()
        return nickname_var, password_var, confirm_password_var, gmail_var, name_var, apellidos_var

    def comprobar_registro(self):
        nickname_var, password_var, confirm_password_var, gmail_var, name_var, apellidos_var = self.recoger_datos_registro()
        if (nickname_var == '' or password_var == '' or confirm_password_var == '' 
        or gmail_var == '' or name_var == '' or apellidos_var == ''):
            campos_obligatorios = QMessageBox.warning(None, "Error", "Debes rellenar todos los campos")
        elif self.validador.validar_contrasenia(password_var) or self.validador.validar_contrasenia(confirm_password_var):
            advertencia = QMessageBox.warning(None, "Contraseña incorrecta", "La cadena tiene que contener al menos \n  8 dígitos tanto letras como dígitos")
        elif password_var != confirm_password_var:
            password_desigual = QMessageBox.warning(None, "Error", "No coinciden las contraseñas")
        else:
            if self.almacen_usuarios.add_usuario(nickname_var, password_var, gmail_var, name_var, apellidos_var):
                adicion_correcta = QMessageBox.information(None, "Usuario Añadido", "Usuario añadido con éxito")
                self.volver_al_menu()
            else:
                adicion_correcta = QMessageBox.information(None, "Usuario Incorrecto", "El usuario ya está añadido")

    def volver_al_menu(self):
        self.form.hide()
        self.parent().setVisible(True)
        #nickname_var, password_var = self.recoger_campos_boton_iniciar_sesion()
        #if not(self.validador.validar_password(password_var)):






