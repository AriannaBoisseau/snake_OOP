import Board
import Snake
import Apple
import Position
import SquareValue

from typing import List
import random

class Game:
    def __init__(self):
        self.board = Board.Board()
        self.snake = Snake.Snake()

    def run(self):

        for piece in self.snake.body:
            if piece == self.snake.body[0]:
                self.board.set_square_value(piece, SquareValue.Square_value.HEAD) 
            else:
                self.board.set_square_value(piece, SquareValue.Square_value.SNAKE)

        empty_squares = []
        for x in range(self.board.width):
            for y in range(self.board.height):
                pos = Position.Position(x, y)
                if self.board.grid[x][y].value == SquareValue.Square_value.EMPTY:
                    empty_squares.append(pos)
        
        apple_position = empty_squares[random.randint(0, len(empty_squares))]
        
        # oggetto apple non è mai usato ?????????????
        apple = Apple.Apple(position=apple_position)
        self.board.set_square_value(apple_position, SquareValue.Square_value.FOOD)

        
