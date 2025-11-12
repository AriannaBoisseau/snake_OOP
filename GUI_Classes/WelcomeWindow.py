from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import webbrowser

from GUI_Classes.GameWindow import GameWindow

class WelcomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Snake Game")
        self.setStyleSheet("background-color: black;")
        self.setFixedSize(900, 900)

        # central widget
        central_widget = QWidget()
        layout = QVBoxLayout()

        # title image
        label = QLabel(self)
        pixmap = QPixmap('assets/title_rainbow.png')
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.addWidget(label)

        # start game button
        button = QPushButton("Start Game!")
        button.setFixedSize(200, 100)
        button.setStyleSheet("font-size: 24px;")
        layout.addWidget(button, alignment=(Qt.AlignHCenter | Qt.AlignCenter))
        button.clicked.connect(self.start_game)

        # credits button
        credits_button = QPushButton("Credits")
        credits_button.setFixedSize(200, 50)
        credits_button.setStyleSheet("font-size: 18px;")
        layout.addWidget(credits_button, alignment=(Qt.AlignHCenter | Qt.AlignCenter))
        credits_button.clicked.connect(self.show_credits)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_game(self):
        self.hide()
        self.game_window = GameWindow()
        self.game_window.show()

    def show_credits(self):
        webbrowser.open('https://github.com/AriannaBoisseau/snake_OOP')