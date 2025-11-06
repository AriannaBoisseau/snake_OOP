from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Snake Game")
        self.setStyleSheet("background-color: black;")
        self.setFixedSize(1200, 700)

        # central widget
        central_widget = QWidget()
        layout = QVBoxLayout()

        # image
        label = QLabel(self)
        pixmap = QPixmap('assets/title_rainbow.png')
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.addWidget(label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)