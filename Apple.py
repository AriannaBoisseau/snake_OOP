import Position

class Apple:
    def __init__(self, position: Position, points = 1, is_eatean = False):
        self.position = position
        self.points = points
        self.is_eatean = is_eatean