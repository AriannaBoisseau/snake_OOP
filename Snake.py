import Position
import Direction

class Snake:
    def __init__(self, lenght = 5, body = [Position.Position(5, 5), Position.Position(5, 4), Position.Position(5, 3), Position.Position(5, 2), Position.Position(5, 1)], direction = Direction.Direction.EAST):
        self.lenght = lenght
        self.body = body
        self.direction = direction

snake = Snake()

print("Snake length:", snake.lenght)
print("Snake body:", snake.body)
print("Snake direction:", snake.direction)