"""
Sign your name:Zachary Blum

Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!

"""
import arcade

SW = 500
SH = 500
blue_box_SPEED = 4
red_box_SPEED = 3


class Box:
    def __init__(self, pos_x, pos_y, dx, dy, height, width, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.height = height
        self.width = width
        self.col = col

    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.height, self.width, self.col)

    def update(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_x < self.width:
            self.dx = 0
            self.pos_x = self.width

        elif self.pos_x > SW - self.width:
            self.pos_x = SW - self.width
            self.dx = 0

        elif self.pos_y > SH - self.height:
            self.dy = 0
            self.pos_y = SH - self.height

        elif self.pos_y < self.height:
            self.dy = 0
            self.pos_y = self.height


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.GOLD)
        self.blue_box = Box(300, 250, 0, 0, 30, 30, arcade.color.BLUE)
        self.red_box = Box(250, 300, 0, 0, 30, 30, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.red_box.draw()
        self.blue_box.draw()

    def on_update(self, dt):
        self.blue_box.update()
        self.red_box.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.blue_box.dy = blue_box_SPEED
        elif key == arcade.key.DOWN:
            self.blue_box.dy = -blue_box_SPEED
        elif key == arcade.key.LEFT:
            self.blue_box.dx = -blue_box_SPEED
        elif key == arcade.key.RIGHT:
            self.blue_box.dx = blue_box_SPEED
        if key == arcade.key.W:
            self.red_box.dy = red_box_SPEED
        elif key == arcade.key.S:
            self.red_box.dy = -red_box_SPEED
        elif key == arcade.key.A:
            self.red_box.dx = -red_box_SPEED
        elif key == arcade.key.D:
            self.red_box.dx = red_box_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.blue_box.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.blue_box.dy = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.red_box.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.red_box.dy = 0


def main():
    window = MyGame(SW, SH, "Jedi Training")
    arcade.run()


if __name__ == "__main__":
    main()
