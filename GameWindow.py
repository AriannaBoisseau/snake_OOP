from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import SquareValue
import Game

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

        self.game = Game.Game()
        self.game.run()

        self.draw_board(layout)

    def draw_board(self, layout):

        board_widget = QWidget()
        board_layout = QGridLayout()
        board_layout.setSpacing(0)

        for y in range(self.game.board.height):
            for x in range(self.game.board.width):
                square = self.game.board.grid[x][y]
                label = QLabel()
                label.setFixedSize(15, 15)
                label.setAlignment(Qt.AlignCenter)
                
                if square.value == SquareValue.Square_value.BORDER:
                    label.setStyleSheet("background-color: white;")
                elif square.value == SquareValue.Square_value.SNAKE:
                    label.setStyleSheet("background-color: green;")
                elif square.value == SquareValue.Square_value.FOOD:
                    label.setStyleSheet("background-color: red;")
                elif square.value == SquareValue.Square_value.HEAD:
                    label.setStyleSheet("background-color: yellow;")
                else:
                    pass
                
                board_layout.addWidget(label, y, x)

        board_widget.setLayout(board_layout)
        layout.addWidget(board_widget, alignment=Qt.AlignCenter)
