import Classes.Direction as Direction
import Classes.Game as Game
import Classes.SquareValue as SquareValue
import GUI_Classes.Gui as Gui

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

    stdscr.clear()

    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input
    stdscr.timeout(100)  # Refresh every 100ms

    game = Game.Game()

    game.run()
    
    direction = game.snake.direction  # Initialize direction

    while True:
        # stdscr.clear()

        stdscr.border(0)
        stdscr.addstr(0, 2, ascii_art)
        stdscr.addstr(0, 2, '~ Welcome to Snake Game ~')
        stdscr.addstr(7, 2, "Use arrow keys to move the snake ~ Press \"q\" to quit the game")
        stdscr.addstr(8, 2, "Points: {}".format(game.points))

        # Handle input
        key = stdscr.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if key == curses.KEY_UP and direction != Direction.Direction.SOUTH:
                direction = Direction.Direction.NORTH
            elif key == curses.KEY_DOWN and direction != Direction.Direction.NORTH:
                direction = Direction.Direction.SOUTH
            elif key == curses.KEY_LEFT and direction != Direction.Direction.EAST:
                direction = Direction.Direction.WEST
            elif key == curses.KEY_RIGHT and direction != Direction.Direction.WEST:
                direction = Direction.Direction.EAST
        elif key == ord('q'):
            break

        # update snake direction and move
        game.snake.direction = direction
        game.snake.move()

        # Update snake body display
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
                    char = '#'
                elif square.value == SquareValue.Square_value.SNAKE:
                    char = 'S'
                elif square.value == SquareValue.Square_value.FOOD:
                    char = 'A'
                elif square.value == SquareValue.Square_value.HEAD:
                    char = 'H'
                else:
                    char = '.'
                
                stdscr.addch(y + 10, (x * 2) + 7, char) 

        game.update_board()

        # detect collision AFTER moving
        try:
            game.detect_collision()
        except Exception as e:
            if str(e) == "FoodEaten":
                stdscr.addstr(8, 2, "Points: {}".format(game.points))
            elif str(e) == "CannotEatYourself" or str(e) == "GameOver":
                stdscr.clear()
                stdscr.addstr(10, 10, "Game over! Current points: {}".format(game.points))
                stdscr.addstr(12, 10, "Press any key to play again...")
                stdscr.addstr(14, 10, "Press 'q' to quit.")
                stdscr.nodelay(False)
                key = stdscr.getch()
                if key == ord('q'):
                    return
                else:
                    # restarting game
                    main(stdscr)
                    return

            else:
                stdscr.addstr(8, 2, "Unexpected error: {}".format(str(e)))

        # update terminal
        stdscr.refresh()
        time.sleep(0.1)

if __name__ == "__main__":

    print("Welcome to Snake Game!")
    print("Press 1 to play in terminal.")
    print("Press 2 to play in GUI.")
    choice = input("Enter your choice (1 or 2): ")
    # choice = '2'
    if choice == '1':
        try:
            curses.wrapper(main)
        except Exception as e:
            print('The terminal window is too small to run the game.')
            print('Put the terminal window in full screen or make the font smaller and try again!')
    elif choice == '2':
        gui = Gui.Gui()
        gui.run()
    else:
        print("Invalid choice. Exiting the game.")