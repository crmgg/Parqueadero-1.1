from PyQt5.QtWidgets import QMainWindow

class VistaUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vista Usuario")
        self.setGeometry(100, 100, 400, 300)
