import Board
import Snake
import Apple
import Position
from typing import List

class Game:
    def __init__(self, board: Board.Board, snake: Snake.Snake, apples: List[Apple.Apple]):
        self.board = board
        self.snake = snake
        self.apples = apples

    def run(self):
        board = Board.Board()
        snake = Snake.Snake()
        apple1 = Apple.Apple(position=Position.Position(3, 4))
        apple2 = Apple.Apple(position=Position.Position(7, 8), points=5)
        game = Game(board, snake, [apple1, apple2])

        print("Game started!")

        board.display()
        

