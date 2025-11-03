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
        self.apple = Apple.Apple(position=Position.Position(0,0))
        self.points = 0

    def get_empty_squares(self):
        empty_squares: List[Position.Position] = []
        for x in range(self.board.width):
            for y in range(self.board.height):
                pos = Position.Position(x, y)
                if self.board.grid[x][y].value == SquareValue.Square_value.EMPTY:
                    empty_squares.append(pos)
        return empty_squares

    def run(self):
        for piece in self.snake.body:
            if piece == self.snake.body[0]:
                self.board.set_square_value(piece, SquareValue.Square_value.HEAD) 
            else:
                self.board.set_square_value(piece, SquareValue.Square_value.SNAKE)

        empty_squares = self.get_empty_squares()
        
        apple_position = empty_squares[random.randint(0, len(empty_squares))]
        
        self.apple = Apple.Apple(position=apple_position)
        self.board.set_square_value(apple_position, SquareValue.Square_value.FOOD)

    def update_board(self):
        for x in range(self.board.width):
            for y in range(self.board.height):
                pos = Position.Position(x, y)
                if pos not in self.snake.body and self.board.grid[x][y].value == SquareValue.Square_value.SNAKE:
                    self.board.set_square_value(pos, SquareValue.Square_value.EMPTY)

    def detect_collision(self):
        if self.snake.body[0].x == self.apple.position.x and self.snake.body[0].y == self.apple.position.y:
            # raise foodEaten event
            self.apple.is_eatean = True
            self.snake.lenght += self.apple.points
            self.snake.body.append(self.snake.body[-1])
            self.points += self.apple.points
            # spawn new apple
            empty_squares = self.get_empty_squares()
            apple_position = empty_squares[random.randint(0, len(empty_squares))]
            self.apple = Apple.Apple(position=apple_position)
            self.board.set_square_value(apple_position, SquareValue.Square_value.FOOD)
            # update empty squares
            self.update_board()
            raise Exception("FoodEaten")
        elif self.snake.body[0] in self.snake.body[1:]:
            # raise gameOver event
            raise Exception("CannotEatYourself")
        elif (self.snake.body[0].x == 0 or self.snake.body[0].x == self.board.width - 1 or
              self.snake.body[0].y == 0 or self.snake.body[0].y == self.board.height - 1):
            # raise gameOver event
            raise Exception("GameOver")
        else:
            return None

            

