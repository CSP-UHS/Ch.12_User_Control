'''
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.

Try to make it from the bottom left to the bottom right

'''
import arcade

SW = 640
SH = 480
SPEED = 3  # 3 x 60 = 180 pixels/second


class Ball:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.laser = arcade.load_sound("Sounds/laser.mp3")
        self.explosion = arcade.load_sound("Sounds/explosion.mp3")

    def draw(self):
        arcade.draw_rectangle_filled(SW / 2, SH * 5 / 6, SW, SH / 5, arcade.color.OCEAN_BOAT_BLUE)
        arcade.draw_rectangle_filled(SW / 2, SH / 3, SW, SH / 5, arcade.color.OCEAN_BOAT_BLUE)
        arcade.draw_rectangle_filled(SW / 10, SH / 3, SW / 10, SH / 5, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(SW / 10, SH - 80, SW / 10, SH / 5, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(SW / 3, SH - 80, SW / 10, SH / 5, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(SW - 60, SH - 80, SW / 10, SH / 5, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(SW - 200, SH - 80, SW / 10, SH / 5, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(SW - 60, SH / 3, SW / 10, SH / 5, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(300, 0, 400, 225, arcade.color.RED)
        arcade.draw_rectangle_filled(120, SH / 2 + 40, 30, 145, arcade.color.RED)
        arcade.draw_rectangle_filled(500, SH / 2 + 40, 30, 145, arcade.color.RED)
        arcade.draw_rectangle_filled(320, SH, 150, 65, arcade.color.RED)
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_x < self.rad:
            self.dx = 0
            self.pos_x = self.rad

        elif self.pos_x > SW - self.rad:
            self.pos_x = SW - self.rad
            self.dx = 0

        elif self.pos_y > SH - self.rad:
            self.dy = 0
            self.pos_y = SH - self.rad

        elif self.pos_y < self.rad:
            self.dy = 0
            self.pos_y = self.rad

        if 90 < self.pos_x < 520 and 0 < self.pos_y < 120:
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            arcade.play_sound(self.laser, 20, 0, False)
            self.pos_x = 50
            self.pos_y = 50

        elif 90 < self.pos_x < 150 and 200 < self.pos_y < 300:
            arcade.play_sound(self.laser, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 230 < self.pos_x < 410 and 430 < self.pos_y < SH:
            arcade.play_sound(self.laser, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 470 < self.pos_x < 530 and 190 < self.pos_y < 370:
            arcade.play_sound(self.laser, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 80 < self.pos_x < 560 and 120 < self.pos_y < 225:
            arcade.play_sound(self.explosion, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 0 < self.pos_x < 50 and 100 < self.pos_y < 220:
            arcade.play_sound(self.explosion, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 0 < self.pos_x < 50 and 330 < self.pos_y < 370:
            arcade.play_sound(self.explosion, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 605 < self.pos_x < SW and 345 < self.pos_y < 450:
            arcade.play_sound(self.explosion, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 605 < self.pos_x < SW and 100 < self.pos_y < 220:
            arcade.play_sound(self.explosion, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 90 < self.pos_x < 190 and 345 < self.pos_y < 450:
            arcade.play_sound(self.laser, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 230 < self.pos_x < 300 and 345 < self.pos_y < 450:
            arcade.play_sound(self.laser, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 460 < self.pos_x < 560 and 345 < self.pos_y < 450:
            arcade.play_sound(self.explosion, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50

        elif 0 < self.pos_x < 50 and 360 < self.pos_y < 460:
            arcade.play_sound(self.explosion, 20, 0, False)
            print("You hit the edge at (", self.pos_x, ",", self.pos_y, ")")
            self.pos_x = 50
            self.pos_y = 50


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.GREEN)
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.RED_PURPLE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_update(self, dt):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -SPEED
        elif key == arcade.key.RIGHT:
            self.ball.dx = SPEED
        elif key == arcade.key.UP:
            self.ball.dy = SPEED
        elif key == arcade.key.DOWN:
            self.ball.dy = -SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0


def main():
    window = MyGame(SW, SH, "Bridges")
    arcade.run()


if __name__ == "__main__":
    main()
