from PyQt5.QtWidgets import QMainWindow

class VistaAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vista Administrador")
        self.setGeometry(100, 100, 400, 300)
