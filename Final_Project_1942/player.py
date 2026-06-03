"""
Created by Juan José Rosales (100499176) in nov 2022
Universidad Carlos III de Madrid
"""
import pyxel


class Player:
    """
    Class that will contain all the information related to the player
    """
    def __init__(self, x, y):
        self.lives = 3
        self.x = x - self.w / 2
        self.y = y
        self.alive = True
        self.speed = 1.25
        self.red_killed_enemies = 0
        self.loops = 3
        self.in_loop = False
        self.looptime = 0

    @property
    def w(self):
        return 16

    @property
    def h(self):
        return 16

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, value):
        if -3 <= value <= 3 and type(value) == int:
            self.__lives = value
        else:
            raise TypeError(
                "The lives attribute is not correct. Check its type and value")

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
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, value):
        if type(value) == bool:
            self.__alive = value
        else:
            raise TypeError(
                "The alive attribute is not correct. Check its type and value")

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value and (type(value) == int or type(value) == float):
            self.__speed = value
        else:
            raise TypeError(
                "The speed attribute is not correct. Check its type and value")

    @property
    def red_killed_enemies(self):
        return self.__red_killed_enemies

    @red_killed_enemies.setter
    def red_killed_enemies(self, value):
        if 0<= value <=5  and  type(value) == int:
            self.__red_killed_enemies = value
        else:
            raise TypeError("The red_killed_enemies attribute is not correct. Check its type and value")

    @property
    def loops(self):
        return self.__loops

    @loops.setter
    def loops(self, value):
        if 0 <= value <= 3 and type(value) == int:
            self.__loops = value
        else:
            raise TypeError(
                "The loops attribute is not correct. Check its type and value")

    @property
    def in_loop(self):
        return self.__in_loop

    @in_loop.setter
    def in_loop(self, value):
        if type(value) == bool:
            self.__in_loop = value
        else:
            raise TypeError(
                "The in_loop attribute is not correct. Check its type and "
                "value")

    @property
    def looptime(self):
        return self.__looptime

    @looptime.setter
    def looptime(self, value):
        if 0 <= value and type(value) == int:
            self.__looptime = value
        else:
            raise TypeError(
                "The looptime attribute is not correct. Check its type and value")

    def update(self):
        """
        Method that update the values of the player's attribute each frame
        @param: self(object)
        @return:
        """
        if self.in_loop:
            if self.looptime == 100:
                self.in_loop = False
                self.loops -= 1
                self.looptime = 0
            self.looptime += 1
        # Movement of the player by keyboard
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed

        # For the player to not get out of the screen
        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.w)
        self.y = max(self.y, 0)
        self.y = min(self.y, pyxel.height - self.h)

        if self.lives == 0:
            self.alive = False

    def draw(self):
        """
        Method that draw in the screen the player sprite in an x,y position
        @param: self(object
        @return:
        """
        # When the plane is in loop:
        if self.in_loop:
            # Set up the new image position and change direction of images
            u = 16
            dir = -1
            # Depending on the number of frames in the loop  we display the
            # plane in different positions to create the loop of the plane
            if self.looptime <= 20:
                v = 0
            elif 20 < self.looptime <= 80:
                if 0 <= pyxel.frame_count % 9 <= 3:
                    v = 16
                elif 5 <= pyxel.frame_count % 9 <= 9:
                    v = 32
                else:
                    v = 48
            else:
                v = 64
        else:
            # Regular movement, direction and image of the plane
            u = 0
            dir = 1
            # This changes the sprite depending on the frame_count to create
            # the helix movement
            if 0 <= pyxel.frame_count % 16 <= 4:
                v = 0
            elif 5 <= pyxel.frame_count % 16 <= 8:
                v = 16
            elif 9 <= pyxel.frame_count % 16 <= 12:
                v = 32
            else:
                v = 48
        # This draws the plane
        pyxel.blt(self.x, self.y, 1, u, v, self.w, self.h * dir, colkey=6)
