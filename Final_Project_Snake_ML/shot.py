import pyxel


class Shot:
    """
    Class that will contain all the information related to shots
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = True

    @property
    def width(self):
        return 1

    @property
    def height(self):
        return 4

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
    def is_alive(self, value):
        if type(value) == bool:
            self.__is_alive = value
        else:
            raise TypeError("The alive attribute is not correct. It must be a boolean")


class PlayerShot(Shot):
    """
    Subclass of shots that represents the shots of the player
    """

    def update(self):
        """
        Method that update the value of the shots each frame
        @param: self (object)
        @return:
        """
        # Motion of the shot
        self.y -= 2
        # To do not kill enemies that are not in the screen yet
        if self.y < 5:
            self.is_alive = False

    def draw(self):
        """
        Method to draw the shot sprite in the screen
        @param: self (object)
        @return:
        """
        pyxel.blt(self.x, self.y, 1, 0, 64, self.width, -self.height,
                  colkey=6)


class EnemyShot(Shot):
    """
    Subclass of shots that represents the shots of the enemies
    """

    def update(self):
        """
        @param: self (object
        @return:
        """
        self.y += 1.5

    def draw(self):
        """
        Method to draw the shot sprite in the screen
        @param: self (object)
        @return:
        """
        pyxel.blt(self.x, self.y, 1, 0, 64, self.width, self.height,
                  colkey=6)
