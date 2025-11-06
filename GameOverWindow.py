from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class GameOverWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Snake Game")
        self.setStyleSheet("background-color: black;")
        self.setFixedSize(1200, 700)

        # central widget
        central_widget = QWidget()
        layout = QVBoxLayout()

        # title image
        label = QLabel(self)
        pixmap = QPixmap('assets/title_rainbow.png')
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.addWidget(label)

        # text label
        text_label = QLabel("Game Over! Thanks for playing.", self)
        text_label.setStyleSheet("color: white; font-size: 24px;")
        text_label.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        layout.addWidget(text_label)

        # restart game button
        button = QPushButton("Play Again!")
        button.setFixedSize(200, 100)
        button.setStyleSheet("font-size: 24px;")
        layout.addWidget(button, alignment=(Qt.AlignHCenter | Qt.AlignCenter))
        button.clicked.connect(self.play_again)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def play_again(self):
        # i have imported here in order to not create a circular import
        from GameWindow import GameWindow 
        self.close()
        self.game_window = GameWindow()
        self.game_window.show()