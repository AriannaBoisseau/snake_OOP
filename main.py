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

ascii_art = """
        _________              __            
        /   _____/ ____ _____  |  | __ ____   
        \_____  \ /    \\__  \ |  |/ // __ \  
        /        \   |  \/ __ \|    <\  ___/  
        /_______  /___|  (____  /__|_ \\___  > 
                \/     \/     \/     \/    \/  
    """

def main(stdscr):

    # objects initialization
    board = Board.Board()
    snake = Snake.Snake()
    apple1 = Apple.Apple(position=Position.Position(7, 7))
    
    # terminal printing
    stdscr.clear()

    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input
    stdscr.timeout(100)  # Refresh every 100ms
    
    direction = snake.direction  # Initialize direction

    while True:
        stdscr.clear()

        stdscr.border(0)
        stdscr.addstr(0, 2, ascii_art)
        stdscr.addstr(0, 2, '~ Welcome to Snake ~ Press "q" to quit the game ~')

        for piece in snake.body:
            if piece == snake.body[0]:
                board.set_square_value(piece, SquareValue.Square_value.HEAD) 
            else:
                board.set_square_value(piece, SquareValue.Square_value.SNAKE)

        # Draw board
        for x in range(board.width):
            for y in range(board.height):
                square = board.grid[x][y]
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
        snake.direction = direction
        snake.move()

        # update empty squares
        for x in range(board.width):
            for y in range(board.height):
                pos = Position.Position(x, y)
                if pos not in snake.body and board.grid[x][y].value != SquareValue.Square_value.BORDER:
                    board.set_square_value(pos, SquareValue.Square_value.EMPTY)

        
        # update terminal
        stdscr.refresh()
        time.sleep(0.1)

if __name__ == "__main__":

    curses.wrapper(main)





