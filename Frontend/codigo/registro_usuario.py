from PyQt5.QtWidgets import QMainWindow

class RegistroUsuario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro Usuario")
        self.setGeometry(100, 100, 400, 300)
