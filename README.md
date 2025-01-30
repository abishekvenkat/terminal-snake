# Terminal Snake Game

A classic Snake game implementation for the terminal, inspired by the old Nokia mobile game. Built with Python and the `curses` library.

https://github.com/user-attachments/assets/d43d930e-9694-4e0b-85e4-e691188c349d

## Features

- 🐍 Classic snake gameplay mechanics
- 🎮 Arrow key controls
- 🔴 Colored food items
- 🚀 Increasing difficulty (snake speeds up as it grows)
- 💚 Green-colored game over screen
- 🔄 Restart functionality
- 🛑 Prevention of 180-degree turns (can't reverse direction instantly)
- 📊 Score tracking

## Requirements

- Python 3.x
- `curses` library (pre-installed with Python on Unix-based systems)

> [!WARNING]
> Windows Users:  
> The `curses` library is not natively supported on Windows. Consider using:
> - Windows Subsystem for Linux (WSL)
> - [Git Bash](https://gitforwindows.org/)
> - [Cygwin](https://www.cygwin.com/)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abishekvenkat/terminal-snake.git
cd terminal-snake
```
2. Ensure Python 3 is installed:
```bash
python3 --version
```

## How to Play

### Running the Game
```bash
python3 snake_game.py
```
### Controls
↑ : Move Up

↓ : Move Down

← : Move Left

→ : Move Right

R : Restart after game over

Q : Quit game

### Gameplay
- Guide the snake to eat the red food items (π)
- Each food item increases your score and the snake's length
- The snake speeds up progressively as your score increases
- Avoid walls and self-collision
- Game ends if you hit the walls or the snake's body
- Press 'R' to restart or 'Q' to quit after game over

## Known Issues/Limitations
- Limited terminal compatibility (best experienced in Unix-based terminals)
- Screen flicker during redraw (common in terminal games)
- Performance may vary based on terminal emulator

## License
MIT License - see [LICENSE](/LICENSE) file for details

## Acknowledgments
- Inspired by the classic Nokia Snake game
- Built with Python's `curses` library
