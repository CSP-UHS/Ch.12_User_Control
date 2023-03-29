"""
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
DONE Create a background and perhaps animate some objects.
DONE Pick a user control method and navigate an object around your screen.
ISH Make your object more interesting than a ball.
DONE Create your object with a new class.
DONE Perhaps move your object through a maze or move the object to avoid other moving objects.
DONE Incorporate some sound.
DONE Type the directions to this project below:
DIRECTIONS:
----------
Simple
- 2 player game
    - WASD: Purple Ball (bottom left)
    - Arrows: Orange Ball (top right)
- Goal: get to the white box as fast as you can (the whole ball must be in the box to count as a win)
- If you touch the walls, maze borders, or the black blocks in the maze, you will be sent to your starting positions
- Good Luck!
"""
import arcade
import random

SW = 600
SH = 600
SPEED1 = 3
SPEED2 = 3
obstNum = random.randint(1, 2)


class Players():
    def __init__(self, xx, yy, dx, dy, radius, color):
        self.xx = xx
        self.yy = yy
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        self.laser = arcade.load_sound("laser.wav")
        self.explosion = arcade.load_sound("explosion.wav")

    def draw_ball(self):
        arcade.draw_circle_filled(self.xx, self.yy, self.radius, self.color)

    def update_ball(self):
        self.xx += self.dx
        self.yy += self.dy
        # keeping the ball on the screen
        if self.xx < self.radius:
            self.xx = self.radius
            arcade.play_sound(self.laser)
        if self.xx > SW - self.radius:
            self.xx = SW - self.radius
            arcade.play_sound(self.laser)
        if self.yy < self.radius:
            self.yy = self.radius
            arcade.play_sound(self.laser)
        if self.yy > SH - self.radius:
            self.yy = SH - self.radius
            arcade.play_sound(self.laser)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_SEA_GREEN)
        self.player1 = Players(50, 50, 0, 0, 25, arcade.color.BLUE_VIOLET)
        self.player2 = Players(SH - 50, SW - 50, 0, 0, 25, arcade.color.DARK_ORANGE)
        self.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        # background
        arcade.draw_lrtb_rectangle_filled(0, 100, SH, 0, arcade.color.LIGHT_RED_OCHRE)  # left
        arcade.draw_lrtb_rectangle_filled(0, (SW / 3) + (SW / 2), SH, SH - 100, arcade.color.LIGHT_RED_OCHRE)  # top
        arcade.draw_lrtb_rectangle_filled(400, (SW / 3) + (SW / 2), SH, 100, arcade.color.LIGHT_RED_OCHRE)  # right
        arcade.draw_lrtb_rectangle_filled(200, (SW / 3) + (SW / 2), 200, 100, arcade.color.LIGHT_RED_OCHRE)  # bottom
        arcade.draw_lrtb_rectangle_filled(200, 300, SH - 200, 100, arcade.color.LIGHT_RED_OCHRE)  # middle
        # obstacles
        if self.player1.radius >= 17:
            obstSize1 = 30
        else:
            obstSize1 = 45
        if self.player2.radius >= 17:
            obstSize2 = 30
        else:
            obstSize2 = 45

        if obstNum == 1:
            # player 1 (bottom left)
            arcade.draw_lrtb_rectangle_filled(0, obstSize1, 350, 345, (0, 0, 0))  # left
            arcade.draw_lrtb_rectangle_filled(245, 250, SH, SH - obstSize1, (0, 0, 0))  # top
            arcade.draw_lrtb_rectangle_filled((SW / 3) + (SW / 2) - obstSize1, (SW / 3) + (SW / 2), 350, 345,
                                              (0, 0, 0))  # right
            arcade.draw_lrtb_rectangle_filled(245, 250, 100 + obstSize1, 100, (0, 0, 0))  # bottom
            # player 2 (top right)
            arcade.draw_lrtb_rectangle_filled(SW - obstSize2, SW, 350, 345, (0, 0, 0))  # right
            arcade.draw_lrtb_rectangle_filled(345, 350, obstSize2, 0, (0, 0, 0))  # bottom
            arcade.draw_lrtb_rectangle_filled(340, 345, SH - 100, SH - 100 - obstSize2, (0, 0, 0))  # top
            arcade.draw_lrtb_rectangle_filled(100, 100 + obstSize1, 300, 295, (0, 0, 0))  # left
        elif obstNum == 2:
            # player 1 (bottom left)
            arcade.draw_lrtb_rectangle_filled(0, obstSize1, 350, 345, (0, 0, 0))  # left
            arcade.draw_lrtb_rectangle_filled(145, 150, SH, SH - obstSize1, (0, 0, 0))  # top
            arcade.draw_lrtb_rectangle_filled((SW / 3) + (SW / 2) - obstSize1, (SW / 3) + (SW / 2), 450, 445,
                                              (0, 0, 0))  # right
            arcade.draw_lrtb_rectangle_filled(230, 235, 100 + obstSize1, 100, (0, 0, 0))  # bottom
            # player 1 other side
            arcade.draw_lrtb_rectangle_filled(100 - obstSize1, 100, 230, 225, (0, 0, 0))  # left
            arcade.draw_lrtb_rectangle_filled(355, 360, SH - 100 + obstSize1, SH - 100, (0, 0, 0))  # top
            arcade.draw_lrtb_rectangle_filled((SW / 3) + (SW / 2) - 100, (SW / 3) + (SW / 2) - 100 + obstSize1, 250,
                                              245, (0, 0, 0))  # - right
            arcade.draw_lrtb_rectangle_filled(345, 350, 200, 200 - obstSize1, (0, 0, 0))  # bottom
            arcade.draw_lrtb_rectangle_filled(300 - obstSize1, 300, 250, 245, (0, 0, 0))  # middle
            # player 2 (top right)
            arcade.draw_lrtb_rectangle_filled(SW - obstSize2, SW, 350, 345, (0, 0, 0))  # right
            arcade.draw_lrtb_rectangle_filled(340, 345, obstSize2, 0, (0, 0, 0))  # bottom
            arcade.draw_lrtb_rectangle_filled(165, 170, SH - 100, SH - 100 - obstSize2, (0, 0, 0))  # top
            arcade.draw_lrtb_rectangle_filled(100, 100 + obstSize1, 300, 295, (0, 0, 0))  # left
            # player 2 other side
            arcade.draw_lrtb_rectangle_filled(200 - obstSize2, 200, 150, 145, (0, 0, 0))  # left
            arcade.draw_lrtb_rectangle_filled(270, 275, 400 + obstSize2, 400, (0, 0, 0))  # top
            arcade.draw_lrtb_rectangle_filled((SW / 3) + (SW / 2), (SW / 3) + (SW / 2) + obstSize2, 230, 225,
                                              (0, 0, 0))  # right
            arcade.draw_lrtb_rectangle_filled(470, 475, 100, 100 - obstSize2, (0, 0, 0))  # bottom
            arcade.draw_lrtb_rectangle_filled(300, 300 + obstSize1, 360, 355, (0, 0, 0))  # middle
        # winning box area
        arcade.draw_rectangle_filled(250, 350, 98, 98, (92, 234, 226))
        arcade.draw_text("Purple Wins", 208, 350, (0, 0, 0), 12)
        arcade.draw_rectangle_filled(350, 250, 98, 98, (92, 234, 226))
        arcade.draw_text("Orange Wins", 304, 250, (0, 0, 0), 12)
        # borders
        arcade.draw_line(200, 100, (SW / 3) + (SW / 2), 100, (0, 0, 0), 1)  # bottom border (south)
        arcade.draw_line(100, 0, 100, SH - 100, (0, 0, 0), 1)  # left border (east)
        arcade.draw_line(100, SH - 100, ((SW / 3) + (SW / 2) - 100), SH - 100, (0, 0, 0), 1)  # top border (south)
        arcade.draw_line(((SW / 3) + (SW / 2) - 100), 200, ((SW / 3) + (SW / 2) - 100), SH - 100, (0, 0, 0),
                         1)  # right border (west)
        arcade.draw_line(500, 100, 500, 200, (0, 0, 0), 1)  # right border (east)
        arcade.draw_line(300, 200, 400, 200, (0, 0, 0), 1)  # bottom border (north)
        arcade.draw_line(200, 100, 200, 400, (0, 0, 0), 1)  # middle border (west)
        arcade.draw_line(200, 400, 300, 400, (0, 0, 0), 1)  # middle border (north)
        arcade.draw_line(300, 200, 300, 400, (0, 0, 0), 1)  # middle border (east)
        arcade.draw_line(500, 100, 500, SH, (0, 0, 0), 1)  # right border (east)
        # players
        self.player1.draw_ball()
        self.player2.draw_ball()

    def on_update(self, dt):
        self.player1.update_ball()
        self.player2.update_ball()
        # player1 (bottom left) can't veer off course
        if self.player1.xx == self.player1.radius:  # left
            self.player1.xx = 50
            self.player1.yy = 50
        elif self.player1.yy == self.player1.radius:  # bottom
            self.player1.xx = 50
            self.player1.yy = 50
        elif self.player1.yy == SH - self.player1.radius:  # top
            self.player1.xx = 50
            self.player1.yy = 50
        elif self.player1.xx >= ((SW / 3) + (SW / 2)) - self.player1.radius:  # right
            self.player1.xx = 50
            self.player1.yy = 50
        elif 200 >= (self.player1.xx + self.player1.radius) >= 100:  # left-most block's east side
            if self.player1.yy - self.player1.radius <= SH - 100:
                self.player1.xx = 50
                self.player1.yy = 50
            else:
                pass
        elif 300 >= self.player1.xx + self.player1.radius >= 200:  # middle's north side (1) & top's mid-south side (2)
            if 400 - self.player1.radius <= self.player1.yy <= SH - 100 + self.player1.radius:
                self.player1.xx = 50
                self.player1.yy = 50
            else:
                pass
        elif ((SW/3) + (SW/2) - 100) >= self.player1.xx - self.player1.radius >= 300:  # right's west side (1) & top's
            # right-south side (2)
            if 200 <= self.player1.yy - self.player1.radius <= SH - 100:
                self.player1.xx = 50
                self.player1.yy = 50
            else:
                pass
            if 200 <= self.player1.yy + self.player1.radius <= SH - 100:
                self.player1.xx = 50
                self.player1.yy = 50
            else:
                pass
        elif ((SW/3) + (SW/2) - 100) >= self.player1.xx - self.player1.radius >= 300:  # right's west side (1) and top's
            # right-south side (2)
            if 200 <= self.player1.yy - self.player1.radius <= SH - 100:
                self.player1.xx = 50
                self.player1.yy = 50
            else:
                pass
        if (SW / 3) + (SW / 2) >= self.player1.xx + self.player1.radius >= 200:  # bottom's south side
            if 0 <= self.player1.yy - self.player1.radius <= 100:
                self.player1.xx = 50
                self.player1.yy = 50
            else:
                pass
        if ((SW / 3) + (SW / 2) - 100) >= self.player1.xx + self.player1.radius >= 300:  # middle's east side (1)
            if 200 <= self.player1.yy + self.player1.radius <= SH - 110:  # bottom's north side (2)
                self.player1.xx = 50
                self.player1.yy = 50
            else:
                pass
        else:
            pass
        if 200 >= (self.player1.xx - self.player1.radius) >= 100:  # middle block's west side
            if self.player1.yy - self.player1.radius <= SH - 100:
                self.player1.xx = 50
                self.player1.yy = 50
            else:
                pass
        else:
            pass
        # player2 (top right) can't veer off course
        if self.player2.xx <= self.player2.radius + 100:  # left
            self.player2.xx = SW - 50
            self.player2.yy = SH - 50
        elif self.player2.yy == self.player2.radius:  # bottom
            self.player2.xx = SW - 50
            self.player2.yy = SH - 50
        elif self.player2.yy == SH - self.player2.radius:  # top
            self.player2.xx = SW - 50
            self.player2.yy = SH - 50
        elif self.player2.xx == SW - self.player2.radius:  # right
            self.player2.xx = SW - 50
            self.player2.yy = SH - 50
        elif (SW / 3) + (SW / 2) >= self.player2.xx - self.player2.radius >= 400:  # right's west side
            if 100 <= self.player2.yy - self.player2.radius <= SH:
                self.player2.xx = SW - 50
                self.player2.yy = SH - 50
            else:
                pass
        if (SW / 3) + (SW / 2) >= self.player2.xx - self.player2.radius >= 200:  # bottom's north side
            if 100 - self.player2.radius <= self.player2.yy <= 200 - self.player2.radius:
                self.player2.xx = SW - 50
                self.player2.yy = SH - 50
            else:
                pass
        elif 300 >= self.player2.xx + self.player2.radius >= 200:  # left's east side
            if 100 + self.player2.radius <= self.player2.yy <= 400 - self.player2.radius:
                self.player2.xx = SW - 50
                self.player2.yy = SH - 50
            else:
                pass
        if 300 >= self.player2.xx - self.player2.radius >= 200:  # top's south side (1) and middle's west side (2)
            if 200 + self.player2.radius <= self.player2.yy <= 400 + self.player2.radius:
                self.player2.xx = SW - 50
                self.player2.yy = SH - 50
            else:
                pass
        elif (SW / 3) + (
                SW / 2) - self.player2.radius >= self.player2.xx >= 300 + self.player2.radius:  # middle's south side
            if 100 <= self.player2.yy <= 200 + self.player2.radius:
                self.player2.xx = SW - 50
                self.player2.yy = SH - 50
            else:
                pass
        if 450 - self.player2.radius >= self.player2.xx >= 400 - self.player2.radius:  # middle's east side
            if 200 + self.player2.radius <= self.player2.yy <= 500 - self.player2.radius:
                self.player2.xx = SW - 50
                self.player2.yy = SH - 50
            else:
                pass
        elif ((SW / 3) + (
                SW / 2) - 100) - self.player2.radius >= self.player2.xx >= 100 + self.player2.radius:  # top - north
            if 500 - self.player2.radius <= self.player2.yy <= SH - self.player2.radius:
                self.player2.xx = SW - 50
                self.player2.yy = SH - 50
            else:
                pass
        # 1 obstacle
        # - player 1
        if self.player1.radius >= 17:
            obstSize1 = 30
        else:
            obstSize1 = 45
        if self.player1.radius >= 17:
            obstSize2 = 30
        else:
            obstSize2 = 45
        if obstNum == 1:
            if self.player1.xx - self.player1.radius <= obstSize1:  # left
                if 345 - self.player1.radius <= self.player1.yy <= 350 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            if 250 + self.player1.radius >= self.player1.xx >= 245 - self.player1.radius:  # top
                if SH - obstSize1 - self.player1.radius <= self.player1.yy:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif (SW / 3) + (SW / 2) - obstSize1 - self.player1.radius <= self.player1.xx:  # right
                if 345 - self.player1.radius <= self.player1.yy <= 350 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            if 250 + self.player1.radius >= self.player1.xx >= 245 - self.player1.radius:  # top
                if 100 + self.player1.radius <= self.player1.yy <= 100 + obstSize1 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            # - player 2
            if 100 - self.player2.radius <= self.player2.xx <= 100 + obstSize2 + self.player2.radius:  # left
                if 295 - self.player2.radius <= self.player2.yy <= 300 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            # =========================================================================================================
            if 345 + self.player2.radius >= self.player2.xx >= 340 - self.player2.radius:  # top
                print("a")
                if SH - 100 - obstSize2 - self.player2.radius <= self.player2.yy <= SH - 100 - obstSize2:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif SW - obstSize2 - self.player2.radius <= self.player2.xx <= SW:  # right
                if 345 - self.player2.radius - 0.5 <= self.player2.yy <= 350 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            if 350 + self.player2.radius >= self.player2.xx >= 345 - self.player2.radius:  # top
                if self.player2.yy <= obstSize2 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            # if obstNum = 2 obstacles
        elif obstNum == 2:
            if self.player1.xx - self.player1.radius <= obstSize1:  # left
                if 345 - self.player1.radius <= self.player1.yy <= 350 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif 150 + self.player1.radius >= self.player1.xx >= 145 - self.player1.radius:  # top
                if SH - obstSize1 - self.player1.radius <= self.player1.yy:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif (SW / 3) + (SW / 2) - obstSize1 - self.player1.radius <= self.player1.xx:  # right
                if 445 - self.player1.radius <= self.player1.yy <= 450 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif 235 + self.player1.radius >= self.player1.xx >= 230 - obstSize1:  # bottom
                if 100 + self.player1.radius <= self.player1.yy <= 100 + obstSize1 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            # - player 1 other side
            if 100 - obstSize1 <= self.player1.xx + self.player1.radius <= 100:  # left
                if 225 - self.player1.radius <= self.player1.yy <= 230 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif 360 + self.player1.radius + 0.5 >= self.player1.xx >= 355 - self.player1.radius - 0.5:  # top
                if SH - 100 + obstSize1 + self.player1.radius >= self.player1.yy >= SH - 100 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif (SW/3)+(SW/2)-100 + self.player1.radius <= self.player1.xx <= (SW/3)+(SW/2)-100+obstSize1 + self.\
                    player1.radius:  # right
                if 245 - self.player1.radius <= self.player1.yy <= 250 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            if 350 + self.player1.radius >= self.player1.xx >= 345 - self.player1.radius:  # bottom
                if 200 - obstSize1 - self.player1.radius <= self.player1.yy <= 200 - self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            if 300 - obstSize1 - self.player1.radius <= self.player1.xx <= 300 - self.player1.radius:  # middle
                if 245 - self.player1.radius <= self.player1.yy <= 250 + self.player1.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
        # - player 2 ==================================================================================================
            if self.player2.xx - self.player2.radius <= obstSize2 + 100:  # left
                if 295 - self.player2.radius <= self.player2.yy <= 300 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif 170 + self.player2.radius >= self.player2.xx >= 165 - self.player2.radius:  # top
                if SH - 100 - obstSize2 - self.player2.radius <= self.player2.yy <= SH - 100 - self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif SW - obstSize2 - self.player2.radius <= self.player2.xx <= SW - self.player2.radius:  # right
                if 345 - self.player2.radius <= self.player2.yy <= 350 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif 345 + self.player1.radius >= self.player2.xx >= 340 - self.player1.radius:  # bottom
                if self.player2.radius <= self.player2.yy <= obstSize2 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            # - player 2 other side
            if 200 - obstSize2 - self.player2.radius <= self.player2.xx <= 200 - self.player2.radius:  # left
                if 145 - self.player2.radius <= self.player2.yy <= 150 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif 275 + self.player2.radius >= self.player2.xx >= 270 - self.player2.radius:  # top
                if 400 + self.player2.radius <= self.player2.yy <= 400 + obstSize2 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif (SW/3)+(SW/2)+self.player2.radius <= self.player2.xx <= (SW/3)+(SW/2)+obstSize2 + self.player2.radius:
                if 225 - self.player2.radius <= self.player2.yy <= 230 + self.player2.radius:  # right
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            elif 475 + self.player2.radius >= self.player2.xx >= 470 - self.player2.radius:  # bottom
                if 100 - obstSize2 - self.player2.radius <= self.player2.yy <= 100 - self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
            if 300 + self.player2.radius <= self.player2.xx <= 300 + obstSize2 + self.player2.radius:  # middle
                if 355 - self.player2.radius <= self.player2.yy <= 360 + self.player2.radius:
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                else:
                    pass
        # who wins and how
        won = 0
        if 300 - self.player1.radius >= self.player1.xx >= 200 + self.player1.radius:
            if 400 - self.player1.radius >= self.player1.yy >= 300 + self.player1.radius:
                if won == 0:
                    arcade.play_sound(self.player1.explosion, 150)
                    print("Player 1 (Purple Ball) has won!")
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                    won += 1
                else:
                    pass
            else:
                pass
        elif 398 - self.player2.radius >= self.player2.xx >= 302 + self.player2.radius:
            if 298 - self.player2.radius >= self.player2.yy >= 202 + self.player2.radius:
                if won == 0:
                    arcade.play_sound(self.player2.explosion, 200)
                    print("Player 2 (Orange Ball) has won!")
                    self.player1.xx = 50
                    self.player1.yy = 50
                    self.player2.xx = SW - 50
                    self.player2.yy = SH - 50
                    won += 1
                else:
                    pass
            else:
                pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player2.dx = -SPEED1
        elif key == arcade.key.RIGHT:
            self.player2.dx = SPEED1
        elif key == arcade.key.UP:
            self.player2.dy = SPEED1
        elif key == arcade.key.DOWN:
            self.player2.dy = -SPEED1
        if key == arcade.key.A:
            self.player1.dx = -SPEED2
        elif key == arcade.key.D:
            self.player1.dx = SPEED2
        elif key == arcade.key.W:
            self.player1.dy = SPEED2
        elif key == arcade.key.S:
            self.player1.dy = -SPEED2

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player2.dx = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player2.dy = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.player1.dx = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.player1.dy = 0


def main():
    window = MyGame(SW, SH, "User Control Project - HI")
    arcade.run()


if __name__ == "__main__":
    main()
