import Classes.Position as Position
import Classes.Direction as Direction

class Snake:
    def __init__(self, lenght = 5, body = [Position.Position(5, 5), Position.Position(5, 4), Position.Position(5, 3), Position.Position(5, 2), Position.Position(5, 1)], direction = Direction.Direction.SOUTH):
        self.lenght = lenght
        self.body = body
        self.direction = direction

    def move(self):
        head = self.body[0]
        if self.direction == Direction.Direction.NORTH:
            new_head = Position.Position(head.x, head.y - 1)
        elif self.direction == Direction.Direction.SOUTH:
            new_head = Position.Position(head.x, head.y + 1)
        elif self.direction == Direction.Direction.EAST:
            new_head = Position.Position(head.x + 1, head.y)
        elif self.direction == Direction.Direction.WEST:
            new_head = Position.Position(head.x - 1, head.y)
        
        self.body.insert(0, new_head)
        self.body.pop()

    def reset(self):
        self.lenght = 5
        self.body = [Position.Position(5, 5), Position.Position(5, 4), Position.Position(5, 3), Position.Position(5, 2), Position.Position(5, 1)]
        self.direction = Direction.Direction.SOUTH