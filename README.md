# Terminal Snake Game

A classic Snake game implementation for the terminal, inspired by the old Nokia mobile game. Built with Python and the `curses` library.

![Gameplay Demo](https://via.placeholder.com/600x400.png?text=Terminal+Snake+Game+Demo) 
*(Replace with actual gameplay GIF)*

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

**Note for Windows Users:**  
The `curses` library is not natively supported on Windows. Consider using:
- Windows Subsystem for Linux (WSL)
- [Git Bash](https://gitforwindows.org/)
- [Cygwin](https://www.cygwin.com/)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abishekvenkat/terminal-snake.git
cd terminal-snake-game