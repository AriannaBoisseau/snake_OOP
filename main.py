import Apple
import Board
import Direction
import Game
import Position
import Snake
import SquareValue
import Square


import curses
import time
import random

ascii_art = """
        _________              __            
        /   _____/ ____ _____  |  | __ ____   
        \_____  \ /    \\__  \ |  |/ // __ \  
        /        \   |  \/ __ \|    <\  ___/  
        /_______  /___|  (____  /__|_ \\___  > 
                \/     \/     \/     \/    \/  
    """

def main(stdscr):

    # # objects initialization
    # board = Board.Board()
    # snake = Snake.Snake()
    # # iterate on all square of the board and create a list of empty squares
    # empty_squares = []
    # for x in range(board.width):
    #     for y in range(board.height):
    #         pos = Position.Position(x, y)
    #         if board.grid[x][y].value == SquareValue.Square_value.EMPTY:
    #             empty_squares.append(pos)

    # place an apple randomly on an empty square
    # apple_position = empty_squares[random.randint(0, len(empty_squares))]
    # apple = Apple.Apple(position=apple_position)
    # board.set_square_value(apple.position, SquareValue.Square_value.FOOD)
    
    # terminal printing
    stdscr.clear()

    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input
    stdscr.timeout(100)  # Refresh every 100ms

    game = Game.Game()

    game.run()
    
    direction = game.snake.direction  # Initialize direction

    while True:
        stdscr.clear()

        stdscr.border(0)
        stdscr.addstr(0, 2, ascii_art)
        stdscr.addstr(0, 2, '~ Welcome to Snake ~ Press "q" to quit the game ~')

        for piece in game.snake.body:
            if piece == game.snake.body[0]:
                game.board.set_square_value(piece, SquareValue.Square_value.HEAD) 
            else:
                game.board.set_square_value(piece, SquareValue.Square_value.SNAKE)

        # Draw board
        for x in range(game.board.width):
            for y in range(game.board.height):
                square = game.board.grid[x][y]
                if square.value == SquareValue.Square_value.BORDER:
                    char = '█'
                elif square.value == SquareValue.Square_value.SNAKE:
                    char = 'S'
                elif square.value == SquareValue.Square_value.FOOD:
                    char = 'A'
                elif square.value == SquareValue.Square_value.HEAD:
                    char = 'H'
                else:
                    char = '.'
                
                stdscr.addch(y + 10, x + 7, char) 

        # Handle input
        key = stdscr.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if key == curses.KEY_UP:
                direction = Direction.Direction.NORTH
            elif key == curses.KEY_DOWN:
                direction = Direction.Direction.SOUTH
            elif key == curses.KEY_LEFT:
                direction = Direction.Direction.WEST
            elif key == curses.KEY_RIGHT:
                direction = Direction.Direction.EAST
        elif key == ord('q'):
            break

        # update snake
        game.snake.direction = direction
        game.snake.move()

        # update empty squares
        for x in range(game.board.width):
            for y in range(game.board.height):
                pos = Position.Position(x, y)
                if pos not in game.snake.body and game.board.grid[x][y].value == SquareValue.Square_value.SNAKE:
                    game.board.set_square_value(pos, SquareValue.Square_value.EMPTY)

        
        # update terminal
        stdscr.refresh()
        time.sleep(0.1)

if __name__ == "__main__":

    curses.wrapper(main)





