from typing import List
import Classes.Square as Square
import Classes.Position as Position
import Classes.SquareValue as SquareValue

class Board:
    def __init__(self, width= 40, height = 40):
        self.width = width
        self.height = height
        self.grid: List[List[Square.Square]] = [[Square.Square(Position.Position(x, y)) for y in range(height)] for x in range(width)]
        
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or y == 0 or x == width - 1 or y == height - 1:
                    self.grid[x][y].value = SquareValue.Square_value.BORDER
                else:
                    self.grid[x][y].value = SquareValue.Square_value.EMPTY

    def set_square_value(self, position: Position.Position, value: SquareValue.Square_value):
        if 0 <= position.x < self.width and 0 <= position.y < self.height:
            self.grid[position.x][position.y].value = value

    def clear(self):
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                    self.grid[x][y].value = SquareValue.Square_value.BORDER
                else:
                    self.grid[x][y].value = SquareValue.Square_value.EMPTY