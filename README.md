# Python Snake Game

A small Snake game I built in Python with `pygame`.

## Gameplay overview
- Move the snake on a fixed **25px grid**.
- Eat green pellets to grow and increase score.
- Avoid hitting walls or your own body.
- After game over, press **Space** to replay or **Esc** to quit.

## Requirements
- Python **3.10+**
- `pygame`

Install dependencies:

```bash
pip install pygame
```

## Quick start
From the repository root:

```bash
cd "Python Snake Project"
python pyGameProject.py
```

> Important: run from inside `Python Snake Project` so `titleScreen.png` and `EndScreen.png` are found correctly.

## Controls
| Key | Action |
| --- | --- |
| `Space` | Start game (title screen), replay (end screen) |
| `Esc` | Quit from title/end screen |
| `W` | Move up |
| `A` | Move left |
| `S` | Move down |
| `D` | Move right |
| Window close button | Quit |

## Project layout
```text
Python-Snake-Game/
├── README.md
└── Python Snake Project/
    ├── pyGameProject.py
    ├── titleScreen.png
    └── EndScreen.png
```

## Troubleshooting
- **ModuleNotFoundError: pygame**
  - Install with `pip install pygame`.
- **Images not loading**
  - Ensure your terminal is in `Python Snake Project` before running the script.
