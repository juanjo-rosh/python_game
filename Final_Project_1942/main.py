"""
Created by Juan José Rosales (100499176) in nov 2022
Universidad Carlos III de Madrid
"""

import pyxel
from board import Board
# We adjust the size of the screen
WIDTH = 128
HEIGHT = 160

pyxel.init(WIDTH, HEIGHT, fps=60, display_scale=5, title="1942 Game")

pyxel.load("assets/sprites.pyxres")
pyxel.playm(0, loop=True)
# To start the game we invoke the class Board():
Board()

