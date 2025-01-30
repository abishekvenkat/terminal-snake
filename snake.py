import curses
import random

def initialize_game(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Red text on black background (for food)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green text on black background (for game over screen)

    # Initialize the screen
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)  # Initial speed (100ms delay)

    # Initialize the snake
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # Initialize the food
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], curses.ACS_PI | curses.color_pair(1))  # Draw food in red

    # Initialize the direction
    key = curses.KEY_RIGHT

    return w, snake, food, key, sh, sw

def game_over_screen(stdscr, score):
    sh, sw = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(sh // 2, sw // 2 - 5, "GAME OVER!", curses.color_pair(2))  # Green text
    stdscr.addstr(sh // 2 + 1, sw // 2 - 7, f"Your Score: {score}", curses.color_pair(2))  # Green text
    stdscr.addstr(sh // 2 + 3, sw // 2 - 10, "Press 'R' to Restart", curses.color_pair(2))  # Green text
    stdscr.addstr(sh // 2 + 4, sw // 2 - 8, "Press 'Q' to Quit", curses.color_pair(2))  # Green text
    stdscr.refresh()

def main(stdscr):
    while True:
        w, snake, food, key, sh, sw = initialize_game(stdscr)
        score = 0
        base_delay = 100  # Initial delay (100ms)
        speed_increase_interval = 5  # Increase speed every 5 points

        while True:
            # Adjust snake speed based on score
            if score > 0 and score % speed_increase_interval == 0:
                new_delay = max(50, base_delay - (score // speed_increase_interval) * 10)  # Minimum delay of 50ms
                w.timeout(new_delay)

            next_key = w.getch()
            if next_key != -1:
                # Prevent opposite direction movement
                if (key == curses.KEY_RIGHT and next_key != curses.KEY_LEFT) or \
                   (key == curses.KEY_LEFT and next_key != curses.KEY_RIGHT) or \
                   (key == curses.KEY_DOWN and next_key != curses.KEY_UP) or \
                   (key == curses.KEY_UP and next_key != curses.KEY_DOWN):
                    key = next_key

            # Check if the snake hits the wall or itself
            if (
                snake[0][0] in [0, sh - 1] or
                snake[0][1] in [0, sw - 1] or
                snake[0] in snake[1:]
            ):
                break

            # Calculate the new head
            new_head = [snake[0][0], snake[0][1]]
            if key == curses.KEY_DOWN:
                new_head[0] += 1
            if key == curses.KEY_UP:
                new_head[0] -= 1
            if key == curses.KEY_LEFT:
                new_head[1] -= 1
            if key == curses.KEY_RIGHT:
                new_head[1] += 1

            # Insert the new head
            snake.insert(0, new_head)

            # Check if the snake eats the food
            if snake[0] == food:
                score += 1
                food = None
                while food is None:
                    nf = [
                        random.randint(1, sh - 2),
                        random.randint(1, sw - 2)
                    ]
                    food = nf if nf not in snake else None
            else:
                # Move the snake (remove the tail)
                snake.pop()

            # Clear the screen
            w.clear()

            # Draw the food
            w.addch(food[0], food[1], curses.ACS_PI | curses.color_pair(1))

            # Draw the snake
            for segment in snake:
                w.addch(segment[0], segment[1], curses.ACS_CKBOARD)

            # Refresh the screen to update changes
            w.refresh()

        # Game over screen
        game_over_screen(stdscr, score)

        # Wait for user input to restart or quit
        while True:
            choice = stdscr.getch()
            if choice == ord('r') or choice == ord('R'):
                # Reset the game state
                w.clear()
                w.refresh()
                break
            elif choice == ord('q') or choice == ord('Q'):
                return

if __name__ == "__main__":
    curses.wrapper(main)