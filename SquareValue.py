from enum import Enum

class Square_value(Enum):
    EMPTY = 0
    SNAKE = 1
    FOOD = 2
    BORDER = 3
    HEAD = 4

    def __str__(self):
        return self.name