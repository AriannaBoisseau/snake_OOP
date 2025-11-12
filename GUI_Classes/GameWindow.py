from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap, QKeyEvent
from PyQt5.QtCore import Qt, QTimer

import SquareValue
import Game
import Direction
from GUI_Classes.GameOverWindow import GameOverWindow 

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

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.game_loop(layout))
        self.timer.start(100)

    def draw_board(self, layout):

        board_widget = QWidget()
        board_layout = QGridLayout()
        board_layout.setSpacing(0)

        points_label = QLabel(f"Points: {self.game.points}")
        points_label.setStyleSheet("color: white; font-size: 16px;")
        layout.addWidget(points_label, alignment=Qt.AlignHCenter)

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

    def keyPressEvent(self, event):
        direction = self.game.snake.direction
        if isinstance(event, QKeyEvent):
            key = event.key()
            if key in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right]:
                if key == Qt.Key_Up and direction != Direction.Direction.SOUTH:
                    self.game.snake.direction = Direction.Direction.NORTH
                elif key == Qt.Key_Down and direction != Direction.Direction.NORTH:
                    self.game.snake.direction = Direction.Direction.SOUTH
                elif key == Qt.Key_Left and direction != Direction.Direction.EAST:
                    self.game.snake.direction = Direction.Direction.WEST
                elif key == Qt.Key_Right and direction != Direction.Direction.WEST:
                    self.game.snake.direction = Direction.Direction.EAST
            elif key == Qt.Key_Q:
                print("Quitting the game.")
                self.close()

    def update_board_display(self, layout):
        # clear previous board display
        while layout.count() > 1:
            item = layout.takeAt(1)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        self.draw_board(layout)

    def game_loop(self, layout):
        self.game.snake.move()

        # update snake body display
        for piece in self.game.snake.body:
            if piece == self.game.snake.body[0]:
                self.game.board.set_square_value(piece, SquareValue.Square_value.HEAD) 
            else:
                self.game.board.set_square_value(piece, SquareValue.Square_value.SNAKE)

        # update screen
        self.update_board_display(layout)

        self.game.update_board()

        try:
            self.game.detect_collision()
        except Exception as e:
            if str(e) == "FoodEaten":
                pass
            elif str(e) == "CannotEatYourself" or str(e) == "GameOver":
                self.timer.stop()
                self.hide()
                self.game_over_window = GameOverWindow()
                self.game_over_window.show()
            else:
                print(f"Unexpected error: {str(e)}")