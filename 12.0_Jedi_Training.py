"""
Sign your name: Rachel Linthicum

Update the code in this chapter to do the following:
DONE Open a 500px by 500px window.
DONE Change the Ball class to a Box class.
DONE Instantiate two 30px by 30px boxes. One red and one blue.
DONE Make the blue box have a speed of 240 pixels/second --> 4
DONE Make the red box have a speed of 180 pixels/second --> 3
DONE Control the blue box with the arrow keys.
DONE Control the red box with the WASD keys.
DONE Do not let the boxes go off of the screen.
DONE Incorporate different sounds when either box hits the edge of the screen.
DONE Have two people play this TAG game at the same time.
DONE The red box is always "it" and needs to try to catch the blue box.
- When you're done demonstrate to your instructor!
"""
import arcade

SW = 500
SH = 500
SPEED1 = 4
SPEED2 = 3


class Box():
    def __init__(self, xx, yy, width, height, dx, dy, color):  # dx and dy are similar to velocities
        self.xx = xx
        self.yy = yy
        self.w = width
        self.h = height
        self.dx = dx
        self.dy = dy
        self.color = color
        self.laser = arcade.load_sound("laser.wav")
        self.explosion = arcade.load_sound("explosion.wav")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.xx, self.yy, self.w, self.h, self.color)

    def update_box(self):
        self.xx += self.dx
        self.yy += self.dy
        # keeping the box on the screen
        if self.xx - 12 < 0:
            self.xx = (self.w/2) + 2
            arcade.play_sound(self.laser)
        if self.xx + 8 > SW:
            self.xx = SW - (self.w/2) - 2
            arcade.play_sound(self.laser)
        if self.yy - 12 < 0:
            self.yy = (self.h/2) + 2
            arcade.play_sound(self.explosion)
        if self.yy + 8 > SH:
            self.yy = SH - (self.h/2) - 2
            arcade.play_sound(self.explosion)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PALE_TURQUOISE)
        self.box1 = Box(50, 50, 20, 20, 0, 0, arcade.color.BLUE)
        self.box2 = Box(SW - 50, SH - 50, 20, 20, 0, 0, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.box1.draw_box()
        self.box2.draw_box()

    def on_update(self, dt):
        self.box1.update_box()
        self.box2.update_box()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.box1.dx = -SPEED1
        elif key == arcade.key.RIGHT:
            self.box1.dx = SPEED1
        elif key == arcade.key.UP:
            self.box1.dy = SPEED1
        elif key == arcade.key.DOWN:
            self.box1.dy = -SPEED1
        if key == arcade.key.A:
            self.box2.dx = -SPEED2
        elif key == arcade.key.D:
            self.box2.dx = SPEED2
        elif key == arcade.key.W:
            self.box2.dy = SPEED2
        elif key == arcade.key.S:
            self.box2.dy = -SPEED2

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.box1.dx = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.box1.dy = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.box2.dx = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.box2.dy = 0


def main():
    window = MyGame(SW, SH, "Hello!")
    arcade.run()


if __name__ == "__main__":
    main()
