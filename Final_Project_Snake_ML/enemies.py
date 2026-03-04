import pyxel
import random


class Enemy:
    """ This class creates the different enemies """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u = 0
        self.v = 0
        self.w = 0
        self.h = 0
        self.dir = 1
        self.is_alive = True
        self.lives = 0
        self.shot_intervals = 0
        self.points = 0
        self.speed = 0

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
    def u(self):
        return self.__u

    @u.setter
    def u(self, u: int):
        if type(u) != int:
            raise TypeError("The u coordinate must be an integer")
        elif u < 0:
            raise ValueError("The u coordinate is a positive integer")
        else:
            self.__u = u

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v: int):
        if type(v) != int:
            raise TypeError("The v coordinate must be an integer")
        elif v < 0:
            raise ValueError("The v coordinate is a positive integer")
        else:
            self.__v = v

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, w: int):
        if type(w) != int:
            raise TypeError("The width must be an integer")
        elif w < 0:
            raise ValueError("The width is a positive integer")
        else:
            self.__w = w

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h: int):
        if type(h) != int:
            raise TypeError("The height must be an integer")
        elif h < 0:
            raise ValueError("The height is a positive integer")
        else:
            self.__h = h

    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: int):
        if type(dir) != int:
            raise TypeError("The direction must be an integer")
        elif dir != 1 and dir != -1:
            raise ValueError("The direction must be +1 or -1")
        else:
            self.__dir = dir

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool):
        if type(is_alive) != bool:
            raise TypeError("The is_alive attribute must be a boolean")
        else:
            self.__is_alive = is_alive

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, lives: int):
        if type(lives) != int:
            raise TypeError("The number of lives must be an integer")
        elif lives < 0:
            raise ValueError("The number of lives must be positive")
        else:
            self.__lives = lives

    @property
    def shot_intervals(self):
        return self.__shot_intervals

    @shot_intervals.setter
    def shot_intervals(self, shot_intervals: float):
        if type(shot_intervals) != int and type(shot_intervals) != float:
            raise TypeError("The shot interval must be a number")
        elif shot_intervals < 0:
            raise ValueError("The shot interval must be positive")
        else:
            self.__shot_intervals = shot_intervals

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points: int):
        if type(points) != int:
            raise TypeError("The points must be an integer")
        elif points < 0:
            raise ValueError("The points must be positive")
        else:
            self.__points = points

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: float):
        if type(speed) != float and type(speed) != int:
            raise TypeError("The speed must be a number")
        elif speed < 0:
            raise ValueError("The speed must be positive")
        else:
            self.__speed = speed


class Regular(Enemy):
    """ The most basic enemy """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.points = 10
        self.lives = 1
        self.w = 16
        self.h = 16
        self.shot_intervals = 0.6
        self.speed = 1
        self.go_back = False

    @property
    def go_back(self):
        return self.__go_back

    @go_back.setter
    def go_back(self, go_back: bool):
        if type(go_back) != bool:
            raise TypeError("The go_back attribute must be a boolean")
        else:
            self.__go_back = go_back

    def update(self):
        # To make the regular enemy move back to the top of the screen
        self.__move_back()
        # Dies when goes out of screen (up or downwards)
        if self.y > pyxel.height - 1 or self.y < -60:
            self.is_alive = False

        if self.lives == 0:
            self.is_alive = False

    def draw(self):
        # The change of the sprites
        if 0 <= pyxel.frame_count % 9 <= 2:
            self.u = 0
        elif 3 <= pyxel.frame_count % 9 <= 5:
            self.u = 16
        else:
            self.u = 32
        pyxel.blt(self.x, self.y, 2, self.u, self.v, self.w,
                  self.h * self.dir, 0)

    def __move_back(self):
        """
        The regular enemy goes makes a special move (moves upwards)
        randomly
        """
        # When the enemy reaches the half of the screen, it randomly goes back
        if (pyxel.height / 2) <= self.y <= (pyxel.height / 2) + 0.75:
            if random.randint(0, 10) <= 5:
                self.go_back = True
                self.dir = -1
                self.v = 64
                self.shot_intervals = 0
        if not self.go_back:
            self.y += self.speed
        else:
            self.y -= self.speed


class Red(Enemy):
    """
    These enemies appear in groups and moves doing circles, if they all
    are killed, they give a bonus
    """
    def __init__(self, x, y, loop_direction):
        super().__init__(x, y)
        self.points = 20
        self.lives = 1
        self.w = 16
        self.h = 16
        self.v = 16
        self.shot_intervals = 0.3
        self.speed = 1
        self.count = 180
        self.loop_direction = loop_direction
        self.loop = 0
        self.total_loops = random.randint(2, 3)

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count: int):
        if type(count) != int:
            raise TypeError("The speed must be an integer")
        elif count < 0:
            raise ValueError("The speed must be positive")
        else:
            self.__count = count

    @property
    def loop_direction(self):
        return self.__loop_direction

    @loop_direction.setter
    def loop_direction(self, loop_direction: int):
        if type(loop_direction) != int:
            raise TypeError("The loop direction must be an integer")
        elif loop_direction != 1 and loop_direction != -1:
            raise ValueError("The loop direction must be 1 or -1")
        else:
            self.__loop_direction = loop_direction

    @property
    def loop(self):
        return self.__loop

    @loop.setter
    def loop(self, loop: int):
        if type(loop) != int:
            raise TypeError("The loop must be an integer")
        elif loop < 0:
            raise ValueError("The speed must be positive")
        else:
            self.__loop = loop

    @property
    def total_loops(self):
        return self.__total_loops

    @total_loops.setter
    def total_loops(self, total_loops: float):
        if type(total_loops) != int:
            raise TypeError("The total number of loops must be a number")
        elif 0 > total_loops > 3:
            raise ValueError("The total number of loops must be between 0 "
                             "and 3")
        else:
            self.__total_loops = total_loops

    def update(self):
        # Move down, do the number of loops (total_loops) and continue going
        # down.
        if self.loop > self.total_loops:
            self.y += self.speed
        elif 20 < self.y < pyxel.height:
            self.x += pyxel.cos(-1 * self.loop_direction * self.count % 360) \
                      * 0.5 * self.loop_direction
            self.y += pyxel.sin(-1 * self.loop_direction * self.count % 360) \
                      * 0.5 * self.loop_direction
            self.count += 1
        else:
            self.y += self.speed
        # We count when each 360 degree loop is done
        if self.count % 360 == 0:
            self.loop += 1

        if self.y > pyxel.height - 1 or self.y < -60:
            self.is_alive = False
        if self.lives == 0:
            self.is_alive = False

    def draw(self):
        # The change of sprites
        if 0 <= pyxel.frame_count % 9 <= 2:
            self.u = 0
        elif 3 <= pyxel.frame_count % 9 <= 5:
            self.u = 16
        else:
            self.u = 32
        pyxel.blt(self.x, self.y, 2, self.u, self.v, self.w * self.dir, self.h,
                  0)


class Bombardier(Enemy):
    """
    The Bombardier enemies are bigger, shoot double and have more lives
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.points = 50
        self.lives = 12
        self.w = 32
        self.h = 32
        self.v = 32
        self.shot_intervals = 0.6
        self.speed = 0.5

    def update(self):
        # When the bombardier appears on screen, it goes down in zigzag
        if self.y > 0:
            self.y += self.speed
            # modulus of 360 to obtain degrees, multiply by 30 to make it
            # faster and add 30 to start at 90 degrees, so sin(30*3) = 0.
            self.x += pyxel.sin(((self.y + 30) * 3) % 360)
        else:
            self.y += self.speed

        if self.y > pyxel.height - 1 or self.y < -60:
            self.is_alive = False
        if self.lives == 0:
            self.is_alive = False

    def draw(self):
        # The change of sprites
        if 0 <= pyxel.frame_count % 9 <= 2:
            self.u = 0
        elif 3 <= pyxel.frame_count % 9 <= 5:
            self.u = 32
        else:
            self.u = 64
        pyxel.blt(self.x, self.y, 2, self.u, self.v, self.w, self.h, 0)


class SuperBombardier(Enemy):
    """
    The  Super Bombardier is the biggest enemy, with a lot of lives,
    and that shoots 3 bullets at the same time. It comes from the bottom
    of the screen
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.points = 80
        self.lives = 20
        self.w = 48
        self.h = 39
        self.u = 0
        self.shot_intervals = 0
        self.speed = 0.5

    def update(self):
        # It moves upwards without shooting and when it arrives the upper
        # part of the screen starts to shoot until you kill it
        if self.y < 20:
            self.shot_intervals = 0.7
        else:
            self.y -= self.speed

        if self.y < -60:
            self.is_alive = False
        if self.lives == 0:
            self.is_alive = False

    def draw(self):
        # The change of sprites
        if 0 <= pyxel.frame_count % 8 <= 3:
            self.v = 80
        elif 4 <= pyxel.frame_count % 8 <= 7:
            self.v = 120
        if self.y > pyxel.height - 16:
            if pyxel.frame_count % 10 > 1:
                pyxel.blt(self.x + self.w / 2, pyxel.height - 20, 1, 16, 120,
                          16, 16, 0)
        pyxel.blt(self.x, self.y, 2, self.u, self.v, self.w, self.h, 0)
