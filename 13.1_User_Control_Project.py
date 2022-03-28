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

'''
import arcade
import random

SW = 800
SH = 800
SPEED1 = 10
SPEED2 = 4    # 3 x 60 = 180 pixels/second
score = 0
score2 = 0

class Box:
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
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.rad, self.rad*8, self.col)

    def update(self):
        self.pos_y += self.dy
            #arcade.play_sound(self.laser)
        if self.pos_y < self.rad*4:
            self.dy = 0
            self.pos_y = self.rad*4
        elif self.pos_y > SH - self.rad*4:
            self.dy = 0
            self.pos_y = SH - self.rad*4

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
        self.score = 0
        self.score2 = 0

    def draw(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)

    def update(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
        if self.pos_x > SW - self.rad:
            self.dx *= -1
            self.pos_x = SW/2
            self.score += 1
        elif self.pos_x < self.rad:
            self.dx *= -1
            self.pos_x = SW/2
            self.score2 += 1
        elif self.pos_y > SH - self.rad:
            if self.dy >= 7:
                self.dy *= -1
            else:
                self.dy *= -1.1
        elif self.pos_y < self.rad:
            if self.dy >= 7:
                self.dy *= -1
            else:
                self.dy *= -1.1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.BLACK)
        dx = random.randint(-SPEED2,SPEED2)
        dy = random.randint(-SPEED2,SPEED2)
        if dx == 0 and dy == 0:
            dx = 1
            dy = 1
        elif dx == 0:
            dx = 1
        elif dy == 0:
            dy = 1
        self.box = Box(30, SH/2, 0, 0, 10, arcade.color.WHITE)
        self.box2 = Box(SW-30, SH/2, 0, 0, 10, arcade.color.WHITE)
        self.ball = Ball(SW/2, SH/2, dx, dy, 15, arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.box.draw()
        self.box2.draw()
        self.ball.draw()
        arcade.draw_text(str(self.ball.score), (SW/2) - 80, SH - 100, arcade.color.BRICK_RED, 50)
        arcade.draw_text(str(self.ball.score2), (SW/2) + 80, SH -100, arcade.color.BLUE, 50)

    def on_update(self, dt):
        self.box.update()
        self.box2.update()
        self.ball.update()

        #left paddle collision
        if self.ball.pos_x - self.ball.rad <= 30 and (self.ball.pos_y <= self.box.pos_y + 40 and self.ball.pos_y >= self.box.pos_y - 40):
            if self.ball.dx >= 7:
                self.ball.dx *= -1
            else:
                self.ball.dx *= -1.1

        #right paddle collision
        if self.ball.pos_x + self.ball.rad >= SW-30 and (self.ball.pos_y <= self.box2.pos_y + 40 and self.ball.pos_y >= self.box2.pos_y - 40):
            if self.ball.dx >= 7:
                self.ball.dx *= -1
            else:
                self.ball.dx *= -1.1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.box2.dy = SPEED1
        elif key == arcade.key.DOWN:
            self.box2.dy = -SPEED1
        if key == arcade.key.W:
            self.box.dy = SPEED1
        elif key == arcade.key.S:
            self.box.dy = -SPEED1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.box2.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.box2.dy = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.box.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.box.dy = 0

def main():
    window = MyGame(SW, SH, "User Control Project")
    arcade.run()

if __name__=="__main__":
    main()