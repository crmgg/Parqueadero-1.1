from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import sys

# Importar las ventanas de los otros archivos en la carpeta "ventanas"
from ventanas.vista_admin import VistaAdmin
from ventanas.vista_user import VistaUser
from ventanas.registro_usuario import RegistroUsuario
from ventanas.registro_admin import RegistroAdmin

class InicioSesion(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Frontend/inicio_sesion.ui", self)  # Carga el archivo .ui desde la carpeta Frontend

        # Conectar botones a sus respectivas funciones
        self.btn_aceptar_admin.clicked.connect(self.abrir_vista_admin)
        self.btn_aceptar_usuario.clicked.connect(self.abrir_vista_usuario)
        self.btn_registro_usuario.clicked.connect(self.abrir_registro_usuario)
        self.btn_registro_admin.clicked.connect(self.abrir_registro_admin)
        self.btn_cancelar.clicked.connect(self.salir)

    def abrir_vista_admin(self):
        self.vista_admin = VistaAdmin()
        self.vista_admin.show()
        self.close()

    def abrir_vista_usuario(self):
        self.vista_usuario = VistaUser()
        self.vista_usuario.show()
        self.close()

    def abrir_registro_usuario(self):
        self.registro_usuario = RegistroUsuario()
        self.registro_usuario.show()
        self.close()

    def abrir_registro_admin(self):
        self.registro_admin = RegistroAdmin()
        self.registro_admin.show()
        self.close()

    def salir(self):
        respuesta = QMessageBox.question(
            self, "Confirmar salida", "¿Estás seguro de que deseas salir?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            sys.exit()

# Asegúrate de tener un bloque para ejecutar la aplicación
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = InicioSesion()
    window.show()
    sys.exit(app.exec_())
