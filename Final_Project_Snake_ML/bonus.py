"""
Created by Alejandro Barroso num:499081 in 08 dic 2022
Universidad Carlos III de Madrid
"""
import pyxel
from player import Player

class Bonus:
    """
    This class groups all the different bonus that the red enemies can give
    """
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.is_alive = True
        self.__player = player

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        if type(x) != float and type(x) != int:
            raise TypeError("The x position must be a number")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        if type(y) != float and type(y) != int:
            raise TypeError("The y position must be a number")
        else:
            self.__y = y

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool):
        if type(is_alive) != bool:
            raise TypeError("The is_alive attribute must be a boolean")
        else:
            self.__is_alive = is_alive

    def update(self):
        # Detects if the player takes the bonus
        if (self.x - 5 + 11 > self.__player.x
                and self.__player.x + 15 > self.x - 5
                and self.y - 5 + 11 > self.__player.y
                and self.__player.y + 15 > self.y + 11):
            self.is_alive = False
        # Move slowly the bonus
        self.y += 0.5


class BonusShot(Bonus):
    """
    The bonus of shooting gives the player more bullets per shot
    """
    def draw(self):
        # The sprites (before and after the player takes it)
        if self.is_alive:
            pyxel.blt(self.x, self.y, 1, 16, 136, 9, 8, 0)
        else:
            pyxel.blt(self.x, self.y, 1, 200, 200, 1, 1, 0)


class BonusLive(Bonus):
    """
    The lives bonus gives an extra live if the player have less than 3
    """
    def draw(self):
        # The sprites (before and after the player takes it)
        if self.is_alive:
            pyxel.blt(self.x, self.y, 1, 0, 136, 10, 8, 0)
        else:
            pyxel.blt(self.x, self.y, 1, 200, 200, 1, 1, 0)


class BonusLoop(Bonus):
    """
    The loop bonus gives the player an extra loop if he has less than 3
    """
    def draw(self):
        # The sprites (before and after the player takes it)
        if self.is_alive:
            pyxel.blt(self.x, self.y, 1, 0, 120, 9, 8, 0)
        else:
            pyxel.blt(self.x, self.y, 1, 200, 200, 1, 1, 0)


class BonusSpeed(Bonus):
    """
    The speed bonus gives the player more moving speed.
    """
    def draw(self):
        # The sprites (before and after the player takes it)
        if self.is_alive:
            pyxel.blt(self.x, self.y, 1, 32, 136, 9, 8, 0)
        else:
            pyxel.blt(self.x, self.y, 1, 200, 200, 1, 1, 0)
