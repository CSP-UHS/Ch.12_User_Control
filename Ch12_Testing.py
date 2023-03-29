# User Control Testing
import arcade
# import random

SW = 640
SH = 480
SPEED1 = 6
SPEED2 = 3


class Ball():
    def __init__(self, xx, yy, dx, dy, radius, color):  # dx and dy are similar to velocities
        self.xx = xx
        self.yy = yy
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        self.laser = arcade.load_sound("laser.wav")
        # two dots (..) and a slash (/) == ../ to get out of a folder then list the folder you want to use
        # "../images/sprite.jpg"
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
            # don't put true on looping (for play_sound) it will crash the screen
        if self.xx > SW - self.radius:
            self.xx = SW - self.radius
            arcade.play_sound(self.laser)
        if self.yy < self.radius:
            self.yy = self.radius
            arcade.play_sound(self.explosion)
        if self.yy > SH - self.radius:
            self.yy = SH - self.radius
            arcade.play_sound(self.explosion)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AO)
        self.ball1 = Ball(50, 50, 0, 0, 15, arcade.color.STIZZA)
        self.ball2 = Ball(SW - 50, SH - 50, 0, 0, 15, arcade.color.DESIRE)
        self.set_mouse_visible(False)
        # don't want to see the cursor: false (see it when hovering over pycharm, but not on the animation screen)

        # self.ball_list = []
        # for i in range(50):
        #     rad = random.randint(10, 30)
        #     x = random.randint(rad, SW - rad)
        #     y = random.randint(rad, SH - rad)
        #     vx = random.randint(-2, 4)
        #     if vx == 0:
        #         vx = 1
        #     vy = random.randint(-2, 4)
        #     if vy == 0:
        #         vy = 1
        #     c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        #     self.ball = Ball(x, y, vx, vy, rad, c)
        #     self.ball_list.append(self.ball)

    def on_draw(self):  # can't rename on_draw
        arcade.start_render()
        self.ball1.draw_ball()
        self.ball2.draw_ball()
        # for item in self.ball_list:
        #     item.draw_ball()

    def on_update(self, dt):  # dt = __/60th <-- updating the screen 60 times a second
        self.ball1.update_ball()
        self.ball2.update_ball()
        # for item in self.ball_list:
        #     item.update_ball()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball1.dx = -SPEED1
        elif key == arcade.key.RIGHT:
            self.ball1.dx = SPEED1
        elif key == arcade.key.UP:
            self.ball1.dy = SPEED1
        elif key == arcade.key.DOWN:
            self.ball1.dy = -SPEED1
        if key == arcade.key.A:
            self.ball2.dx = -SPEED2
        elif key == arcade.key.D:
            self.ball2.dx = SPEED2
        elif key == arcade.key.W:
            self.ball2.dy = SPEED2
        elif key == arcade.key.S:
            self.ball2.dy = -SPEED2

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball1.dx = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball1.dy = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.ball2.dx = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.ball2.dy = 0

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.ball.xx = x
    #     self.ball.yy = y

    # def on_mouse_press(self, x, y, button, modifiers):
    #     if button == arcade.MOUSE_BUTTON_LEFT:
    #         print("Left Mouse button pressed at", x, y)
    #     elif button == arcade.MOUSE_BUTTON_RIGHT:
    #         print("Right Mouse button pressed at", x, y)  # right click by using 2 fingers then click like normal



def main():
    window = MyGame(SW, SH, "Hello!")
    arcade.run()


if __name__ == "__main__":
    main()
