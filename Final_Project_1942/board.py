import random
import pyxel
from player import Player
from enemies import Regular, Red, Bombardier, SuperBombardier
from shot import PlayerShot, EnemyShot
from blast import Blast
from bonus import BonusShot, BonusLive, BonusSpeed, BonusLoop


class Board:
    # we create the init method
    def __init__(self):
        """
        Defining all the attributes of the board
        """
        # attributes of the screen dimensions
        self.__w = pyxel.width
        self.__h = pyxel.height
        # the y of the tilemap to make the background move.
        self.scroll = 1800
        self.score = 0
        self.high_score = 0
        # We create the scene att. which is 0 for starting screen, 1 for
        # play scene, and 2 for game over scene
        self.scene = 0
        self.__player = Player(pyxel.width / 2, pyxel.height * (3 / 4))
        self.enemies = []
        self.blasts = []
        self.bonus = []
        self.shots = []
        self.instruction_number = 0
        # To start the game we need to invoke the function pyxel.run(update,
        # draw)
        pyxel.run(self.update, self.draw)

    @property
    def instructions(self):
        """
        Creates more random waves of enemies
        return: list
        """
        instructions = [0, 0, 0, 1, 0, 0, 1, 0, 2, 3]
        for i in range(15):
            instructions.append(random.randint(0,3))
        return instructions

    @property
    def scroll(self):
        return self.__scroll

    @scroll.setter
    def scroll(self, scroll: float):
        if type(scroll) != int and type(scroll) != float:
            raise TypeError("The scrolling speed must be a number")
        else:
            self.__scroll = scroll

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score: int):
        if type(score) != int:
            raise TypeError("The score must be an integer")
        elif score < 0:
            raise ValueError("The score is a positive integer")
        else:
            self.__score = score

    @property
    def high_score(self):
        return self.__high_score

    @high_score.setter
    def high_score(self, high_score: int):
        if type(high_score) != int:
            raise TypeError("The high score must be an integer")
        elif high_score < 0:
            raise ValueError("The high score is a positive integer")
        else:
            self.__high_score = high_score

    @property
    def scene(self):
        return self.__scene

    @scene.setter
    def scene(self, scene: int):
        if type(scene) != int:
            raise TypeError("The scene number must be an integer")
        elif 2 < scene < 0:
            raise ValueError("The high score is a positive integer")
        else:
            self.__scene = scene

    @property
    def enemies(self):
        return self.__enemies

    @enemies.setter
    def enemies(self, value):
        if type(value) == list:
            self.__enemies = value
        else:
            raise TypeError("The enemies attribute is not correct. Check its type and value")

    @property
    def blasts(self):
        return self.__blasts

    @blasts.setter
    def blasts(self, value):
        if type(value) == list:
            self.__blasts = value
        else:
            raise TypeError("The blasts attribute is not correct. Check its type and value")

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, value):
        if type(value) == list :
            self.__bonus = value
        else:
            raise TypeError("The bonus attribute is not correct. Check its type and value")

    @property
    def shots(self):
        return self.__shots

    @shots.setter
    def shots(self, value):
        if type(value) == list :
            self.__shots = value
        else:
            raise TypeError("The shots attribute is not correct. Check its type and value")

    @property
    def instruction_number(self):
        return self.__instruction_number

    @instruction_number.setter
    def instruction_number(self, value):
        if  0<=value  and  type(value) == int:
            self.__instruction_number = value
        else:
            raise TypeError("The instruction_number attribute is not "
                            "correct. Check its type and value")

    def __update_list(self, ls: list):
        """
        Updates each element of a list
        :param ls: a list with objects
        """
        for elem in ls:
            elem.update()

    def __draw_list(self, ls: list):
        """
        Function that call to the draw method of each element in the list
        :param ls: a list with objects
        """
        for elem in ls:
            elem.draw()

    def __cleanup_list(self, ls: list):
        """
        Function that remove the elements whose attribute is_alive is false
        :param ls: a list with objects
        """
        i = 0
        while i < len(ls):
            elem = ls[i]
            if not elem.is_alive:
                ls.pop(i)
            else:
                i += 1

    def update(self):
        """
        Method that update all the values related to the board
        @param: self (object)
        @return:
        """
        # If we want to close the game
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Movement of the board
        if self.scroll != 0:
            self.scroll -= 0.5
        else:
            self.scroll = 1800
        # Screen changes (start, game and finish)
        if self.scene == 0:
            self.__update_start()
        elif self.scene == 1:
            self.__update_game()
        elif self.scene == 2:
            self.__update_game_over()

        # Check if player has 0 > lives
        if self.__player.lives < 0:
            self.__player.alive = False

        # Update every element of each list
        self.__update_list(self.enemies)
        self.__update_list(self.shots)
        self.__update_list(self.blasts)
        self.__update_list(self.bonus)

    def __update_start(self):
        """
        Method to update the values of the board in the start screen
        @param: self (object)
        @return:
        """
        # This scene will wait until the player presses the return key,
        # which will start the game (scene 1)
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = 1

    def __update_game(self):
        """
        Method to update the game
        @param: self (object)
        @return:
        """
        self.__player.update()
        # Create a group of enemies each 350 frames
        if pyxel.frame_count % 350 == 0 and pyxel.frame_count != 0:
            self.create_enemy()
        # The shooting
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.shots.append(PlayerShot(self.__player.x +
                                         (self.__player.w / 2),
                                         self.__player.y))
        self.enemy_shooting()
        # The loop:
        if pyxel.btnp(pyxel.KEY_Z) and self.__player.loops > 0:
            self.__player.in_loop = True
        # Collisions
        self.collision_shot_enemy()
        self.collision_player_enemy()
        self.collision_shot_player()
        # Bonus
        self.bonus_upgrades()
        # This will wait until the player loses the game to show the game
        # over scene (scene 2)
        if not self.__player.alive:
            self.scene = 2
        # Delete all the objects that are not being used in the game
        self.__cleanup_list(self.shots)
        self.__cleanup_list(self.enemies)
        self.__cleanup_list(self.blasts)

    def __update_game_over(self):
        """
        Method to update the values when the game is over
        @param: self (object)
        @return:
        """
        # To save the high score
        if self.high_score < self.score:
            self.high_score = self.score
        # Clean lists
        self.enemies = []
        self.blasts = []
        self.bonus = []
        self.shots = []
        # Restart the game
        self.instruction_number = 0
        # To start the game again
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = 0
            self.score = 0
            # Reset the player to alive
            self.__player.alive = True
            self.__player.loops = 3
            self.__player.speed = 1.25
            self.__player.lives = 3
            self.__player.x = pyxel.width / 2 - self.__player.w / 2
            self.__player.y = pyxel.height * (3 / 4)

    def draw(self):
        """
        Method to draw all the sprites to create the complete game
        @param: self (object)
        @return:
        """
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, self.scroll, pyxel.width, pyxel.height)
        pyxel.text(80, 4, f"SCORE {self.score:5}", 7)
        pyxel.text(5, 4, f"HIGH SCORE {self.high_score:5}", 7)
        # For each scene we draw different things on screen, so we create
        # different draw functions for each scene.
        if self.scene == 0:
            self.__draw_start()
        elif self.scene == 1:
            self.__draw_game()
        elif self.scene == 2:
            self.__draw_game_over()

    def __draw_start(self):
        """
        Method to draw the specific sprites of the start screen
        @param: self (object)
        @return:
        """
        # We insert the title of the game "1942"
        pyxel.blt(30, 60, 1, 0, 88, 69, 23, colkey=6)
        # and the instructions to start the game
        pyxel.text(8, 45, "Press Enter to start the game", 10)

    def __draw_game(self):
        """
        Method to draw the sprites of the game
        @param: self (object)
        @return:
        """
        # Draw remaining lives:
        for i in range(self.__player.lives):
            # Create a list with the x position of each one
            x = [pyxel.width - 15, pyxel.width - 25, pyxel.width - 35]
            # Print in the left bottom corner one,two or three lives
            pyxel.blt(x[i], pyxel.height - 10, 1, 0, 136, 10, 8, 0)
        # Draw remaining loops:
        for i in range(self.__player.loops):
            # Create a list with the x position of each one
            x = [5, 15, 25]
            # Print in the left bottom corner one,two or three R
            pyxel.blt(x[i], pyxel.height - 10, 1, 0, 120, 8, 8, 0)

        self.__player.draw()
        self.__draw_list(self.enemies)
        self.__draw_list(self.shots)
        self.__draw_list(self.blasts)
        self.__draw_list(self.bonus)

    def __draw_game_over(self):
        """
        Method to draw the sprites of the game when the game is over
        @param: self (object)
        @return:
        """
        pyxel.blt(30, 60, 1, 0, 112, 64, 8, colkey=0)
        pyxel.text(8, 75, "Press enter to start again :)", 10)

    def create_enemy(self):
        """
        We use a list with instructions to create each wave of enemies
        following the list of instructions
        """
        if self.instructions[self.instruction_number] == 0:
            # Create Regular Enemies
            self.create_regular_enemy()
        elif self.instructions[self.instruction_number] == 1:
            # Create Red Enemies
            self.create_red_enemy()
        elif self.instructions[self.instruction_number] == 2:
            # Create a Bombardier
            self.create_bombardier()
        elif self.instructions[self.instruction_number] == 3:
            # Create a Super Bombardier
            self.create_superbombardier()
        # To start with the instructions again if the list is finished
        if self.instruction_number == len(self.instructions)-1:
            self.instruction_number = 0
        else:
            self.instruction_number += 1
    def create_regular_enemy(self):
        """
        Method that creates Regular enemies, with random positions in the top of the
        screen
        @return:
        """
        for i in range(pyxel.rndi(4, 6)):
            self.enemies.append(
                Regular(random.randrange(15, pyxel.width - 15, 15),
                        random.randrange(-60, 0, 15)))

    def create_red_enemy(self):
        """
        Method that creates Red enemies, with random positions in the top of the
        screen
        @return:
        """
        # Predefined formation for Red enemies
        start_position = random.randint((pyxel.width // 2) - 15,
                                        (pyxel.width // 2) + 15)
        formation = [[-30, -30], [-15, -45], [0, -60], [+15, -45], [+30, -30]]
        # Choose direction of the loop:
        if random.randint(0, 1) == 1:
            loopdirection = -1
        else:
            loopdirection = 1
        # The creation of the 5 red enemies:
        for i in range(5):
            self.enemies.append(Red(start_position + formation[i][0],
                                    formation[i][1], loopdirection))
        # To restart the counter of red enemies killed by the player to give
        # the bonus for killing the whole wave
        self.__player.red_killed_enemies = 0

    def create_bombardier(self):
        """
        Method that creates Bombardier enemies, with random positions in the top of the
        screen
        @return:
        """
        self.enemies.append(
            Bombardier((pyxel.width-32)//2, -32))

    def create_superbombardier(self):
        """
        Method that creates Super bombardier enemies, with random positions at the top of
        the screen
        @return:
        """
        self.enemies.append(
            SuperBombardier(random.randrange(0, pyxel.width - 32),
                            pyxel.height + 10))

    def collision_shot_enemy(self):
        """ This detects if any of the player's shots has hit an enemy,
        and if so, deletes the shot, gains points and substracts a life from
         the enemy """
        for shot in self.shots:
            if isinstance(shot, PlayerShot):
                for enemy in self.enemies:
                    if enemy.x <= shot.x <= (enemy.x + enemy.w) and \
                            enemy.y <= shot.y <= (enemy.y + enemy.h) and \
                            enemy.lives > 0:
                        shot.is_alive = False
                        enemy.lives -= 1
                        if enemy.lives == 0:
                            self.score += enemy.points
                        self.blasts.append(Blast(enemy.x + enemy.w / 2,
                                                 enemy.y + enemy.h / 2))
                        pyxel.play(3, 1)
                        if isinstance(enemy, Red):
                            self.__player.red_killed_enemies += 1
                        if self.__player.red_killed_enemies == 5:
                            self.bonus_creation(enemy)

    def collision_player_enemy(self):
        """ This detects if any of the enemies has hit the player,
        and if so, kills the player """
        for enemy in self.enemies:
            if (self.__player.x + self.__player.w > enemy.x
                    and enemy.x + enemy.w > self.__player.x
                    and self.__player.y + self.__player.h > enemy.y
                    and enemy.y + enemy.h > self.__player.y):
                if not self.__player.in_loop:
                    self.__player.lives -= 1
                    self.blasts.append(Blast(self.__player.x +
                                             self.__player.w / 2,
                                             self.__player.y +
                                             self.__player.h / 2))
                    pyxel.play(3, 1)
                    enemy.is_alive = False
                    self.blasts.append(Blast(enemy.x + enemy.w / 2,
                                             enemy.y + enemy.h / 2))
                    pyxel.play(3, 1)

    def collision_shot_player(self):
        """ This detects if any of the enemies' shots has hit the player,
        and if so, kills the player """
        for shot in self.shots:
            if isinstance(shot, EnemyShot) and \
               self.__player.x <= shot.x <= (self.__player.x +
                                             self.__player.w) \
               and self.__player.y <= shot.y <= (self.__player.y +
                                                self.__player.h):
                if not self.__player.in_loop:
                    self.__player.lives -= 1
                    self.blasts.append(Blast(self.__player.x +
                                             self.__player.w / 2,
                                             self.__player.y +
                                             self.__player.h / 2))
                    pyxel.play(3, 1)
                shot.is_alive = False

    def enemy_shooting(self):
        """ Creates the enemy shots, which change depending on the enemy """
        for enemy in self.enemies:
            t = random.randint(0, 10)
            if isinstance(enemy, Bombardier):
                if pyxel.frame_count % 100 == 0 and 10 * enemy.shot_intervals \
                        > t:
                    self.shots.append(EnemyShot(enemy.x + (enemy.w / 4),
                                                enemy.y + enemy.h))
                    self.shots.append(EnemyShot(enemy.x + (enemy.w * 3/4),
                                                enemy.y + enemy.h))
            elif isinstance(enemy, SuperBombardier):
                if pyxel.frame_count % 80 == 0 and 10 * enemy.shot_intervals \
                        > t:
                    self.shots.append(EnemyShot(enemy.x + (enemy.w / 4),
                                                enemy.y + enemy.h))
                    self.shots.append(EnemyShot(enemy.x + (enemy.w * 3/4),
                                                enemy.y + enemy.h))
                    self.shots.append(EnemyShot(enemy.x + (enemy.w / 2),
                                                enemy.y + enemy.h))
            else:
                if pyxel.frame_count % 120 == 0 and 10 * enemy.shot_intervals \
                        > t:
                    self.shots.append(EnemyShot(enemy.x + (enemy.w / 2),
                                                enemy.y + enemy.h))

    def bonus_creation(self, enemy):
        """
        Method that select randomly one of the 4 types of bonus and append it to the
        bonus list
        @param enemy:
        @return:
        """
        #Select a random number 0-4
        bonus_type = random.randint(0, 3)
        #Check what is the corresponding bonus and append it to the bonus list
        if bonus_type == 0:
            self.bonus.append(BonusSpeed(enemy.x,
                                         enemy.y,
                                         self.__player))
        elif bonus_type == 1:
            self.bonus.append(BonusLive(enemy.x,
                                        enemy.y,
                                        self.__player))
        elif bonus_type == 2:
            self.bonus.append(BonusLoop(enemy.x,
                                        enemy.y,
                                        self.__player))
        elif bonus_type == 3:
            self.bonus.append(BonusShot(enemy.x,
                                        enemy.y,
                                        self.__player))
        # Once the bonus is created, we restore the "red killing points"
        self.__player.red_killed_enemies = 0

    def bonus_upgrades(self):
        """
        Method that go throughout  all the bonus list to implement the bonus effect in the
        game
        @return:
        """
        # Go all throughout the bonus list
        for bonus in self.bonus:
            # the bonus is not alive if the player has taken the upgrade:
            if not bonus.is_alive:
                if isinstance(bonus, BonusShot) and pyxel.btnp(
                        pyxel.KEY_SPACE):
                    self.shots.append(PlayerShot(self.__player.x +
                                                 (self.__player.w / 4),
                                                 self.__player.y))
                    self.shots.append(PlayerShot(self.__player.x +
                                                 (self.__player.w * 3/4),
                                                 self.__player.y))
                elif isinstance(bonus, BonusSpeed):
                    # Adds speed to the player each time he catches this bonus
                    self.__player.speed += 0.5
                    self.bonus.remove(bonus)
                elif isinstance(bonus, BonusLoop):
                    # Adds a loop if the player has used at least 1
                    if self.__player.loops < 3:
                        self.__player.loops += 1
                    self.bonus.remove(bonus)
                elif isinstance(bonus, BonusLive):
                    # Adds a live if the player has lost at least 1
                    if self.__player.lives < 3:
                        self.__player.lives += 1
                    self.bonus.remove(bonus)
