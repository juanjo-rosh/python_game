# 1942 Game

A retro-style vertical scrolling shoot-'em-up inspired by the classic arcade game **1942**, built with Python and [Pyxel](https://github.com/kitao/pyxel).

Pilot your fighter plane across enemy territory, dodge incoming fire, destroy waves of enemies, collect power-ups, and fight your way to the highest score possible.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [How to Play](#how-to-play)
- [Enemies](#enemies)
- [Bonuses & Power-ups](#bonuses--power-ups)
- [Project Structure](#project-structure)
- [Authors](#authors)

---

## Prerequisites

- **Python 3.8 or higher** — [Download Python](https://www.python.org/downloads/)

> **Note:** Pyxel requires Python 3.8+ and supports Windows, macOS, and Linux.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/juanjo-rosh/python_game.git
   cd python_game
   ```

2. **Create a virtual environment** *(recommended)*

   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS / Linux
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   This installs [Pyxel](https://github.com/kitao/pyxel), the retro game engine used to run the game.

---

## Running the Game

Navigate to the game directory and run the main script:

```bash
cd Final_Project_Snake_ML
python main.py
```

The game window will open at a scaled resolution (128 × 160 pixels × 5 display scale).

---

## How to Play

| Action | Key |
|---|---|
| Move up / down / left / right | Arrow keys |
| Shoot | `Space` |
| Perform a barrel roll | `Z` |
| Start game / Restart after Game Over | `Enter` |
| Quit game | `Q` |

### Game Flow

1. **Start Screen** – Press `Enter` to begin.
2. **Game Screen** – Survive enemy waves, shoot enemies to earn points, and collect bonuses.
3. **Game Over Screen** – Your score is compared with the high score. Press `Enter` to play again.

### Scoring

Each enemy type is worth a different number of points:

| Enemy | Points |
|---|---|
| Regular | 10 |
| Red | 20 |
| Bombardier | 50 |
| Super Bombardier | 80 |

### Lives & Barrel Rolls

- You start with **3 lives** and **3 barrel rolls**.
- A barrel roll makes your plane temporarily invulnerable — use it wisely!
- Lives and barrel rolls can be restored by collecting the corresponding bonus items.

---

## Enemies

| Enemy | Description |
|---|---|
| **Regular** | Basic enemy that flies down the screen and randomly retreats back upward. |
| **Red** | Moves in circular loops before continuing downward. Killing all Red enemies in a wave drops a bonus. |
| **Bombardier** | Larger, tougher enemy (12 lives) that descends in a zigzag pattern and fires double shots. |
| **Super Bombardier** | The biggest threat (20 lives). Rises from the bottom and fires three bullets simultaneously once it reaches the top of the screen. |

---

## Bonuses & Power-ups

Bonuses are dropped when a wave of Red enemies is fully destroyed. Collect them before they scroll off screen!

| Bonus | Effect |
|---|---|
| **Extra Shot** | Increases the number of bullets fired per shot. |
| **Extra Life** | Restores one life (up to 3 maximum). |
| **Extra Barrel Roll** | Restores one barrel roll (up to 3 maximum). |
| **Speed Up** | Increases your plane's movement speed. |

---

## Project Structure

```
python_game/
├── Final_Project_Snake_ML/
│   ├── assets/
│   │   └── sprites.pyxres      # Pyxel sprite/tilemap/sound resource file
│   ├── main.py                 # Entry point — initialises Pyxel and starts the game
│   ├── board.py                # Core game logic: scenes, collisions, enemy waves
│   ├── player.py               # Player plane: movement, barrel roll, rendering
│   ├── enemies.py              # Enemy classes: Regular, Red, Bombardier, SuperBombardier
│   ├── shot.py                 # Bullet classes: PlayerShot, EnemyShot
│   ├── blast.py                # Explosion effect rendered on enemy/player death
│   └── bonus.py                # Power-up classes dropped by Red enemy waves
├── Final_Project_Report.pdf    # Full project report
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## Authors

Developed by **Juan José Rosales** and **Alejandro Barroso** as a final project at
[Universidad Carlos III de Madrid](https://www.uc3m.es/) (November – December 2022).
