import Position
import SquareValue

class Square:
    def __init__(self, position = Position.Position(0, 0), value = SquareValue.Square_value.EMPTY):
        self.position = position
        self.value = value