"""
Created by Alejandro Barroso num:499081 in 06 dic 2022
Universidad Carlos III de Madrid
"""
import pyxel


class Blast:
    """
    Class that will be called each frame to update and draw all the blasts
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.is_alive = True
        self.count = 0

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
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        if type(width) != int:
            raise TypeError("The width must be an integer")
        elif width < 0:
            raise ValueError("The widthis a positive integer")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        if type(height) != int:
            raise TypeError("The height must be an integer")
        elif height < 0:
            raise ValueError("The height is a positive integer")
        else:
            self.__height = height

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, value):
        if type(value) == bool:
            self.__is_alive = value
        else:
            raise TypeError("The alive attribute is not correct. It must be a boolean")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if 0 <= value and (type(value) == int or type(value == float)):
            self.__radius = value
        else:
            raise TypeError(
                "The radius attribute is not correct. Check that it is a value greater than 0")

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        if 0 <= value and type(value) == int:
            self.__count = value
        else:
            raise TypeError("The radius attribute is not correct. Check that it is an "
                            "integer greater than 0")

    def update(self):
        """
        Method to update all the values of the blasts
        @param: self (object)
        @return:
        """
        # The steps are 0.25 per frame, the duration of the blast will be 10/0.25 frames
        # We can compute the 40 frames computing self.radius * 4
        self.radius += 0.25
        if self.radius > 10:
            self.is_alive = False

    def draw(self):
        """
        Method to draw the blasts
        @param : self (object)
        @return:
        """
        frames = self.radius*4
        # This part will create 4 circles with their circumference in another color
        # from the frame 6 to 40
        if 5 < frames:
            self.y -= self.radius / 20
            pyxel.circ(self.x + 2, self.y, self.radius - 4, 13)
            pyxel.circb(self.x + 2, self.y, self.radius - 4, 0)
            pyxel.circ(self.x - 2, self.y, self.radius - 4, 13)
            pyxel.circb(self.x - 2, self.y, self.radius - 4, 0)
            pyxel.circ(self.x, self.y + 1, self.radius - 4, 13)
            pyxel.circb(self.x, self.y + 1, self.radius - 4, 0)
            pyxel.circ(self.x, self.y - 4, self.radius - 4, 13)
            pyxel.circb(self.x, self.y - 4, self.radius - 4, 0)
        # This part will create 4 circles with their circumference in another color
        # until the frame 30
        if frames< 30:
            pyxel.circ(self.x + 2, self.y, self.radius, 10)
            pyxel.circb(self.x + 2, self.y, self.radius, 8)
            pyxel.circ(self.x - 2, self.y, self.radius, 10)
            pyxel.circb(self.x - 2, self.y, self.radius, 8)
            pyxel.circ(self.x, self.y + 2, self.radius, 10)
            pyxel.circb(self.x, self.y + 2, self.radius, 8)
            pyxel.circ(self.x, self.y - 2, self.radius, 10)
            pyxel.circb(self.x, self.y - 2, self.radius, 8)


