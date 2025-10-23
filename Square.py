import Position
import Square_value

class Square:
    def __init__(self, position = Position.Position(), value = Square_value.Square_value.EMPTY):
        self.position = position
        self.value = value