from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        self.setBaseSize(QSize(400, 400))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()