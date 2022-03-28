'''
Sign your name:Will Jacobson
 
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

'''
import arcade

SW = 500
SH = 500
SPEED1 = 3
SPEED2 = 4    # 3 x 60 = 180 pixels/second

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
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.rad, self.rad, self.col)

    def update(self):
        self.pos_y += self.dy
        self.pos_x += self.dx
        if self.pos_x < self.rad:
            self.dx = 0
            self.pos_x = self.rad
            arcade.play_sound(self.laser)
        elif self.pos_x > SW-self.rad:
            self.dx = 0
            self.pos_x = SW-self.rad
            arcade.play_sound(self.laser)
        elif self.pos_y < self.rad:
            self.dy = 0
            self.pos_y = self.rad
            arcade.play_sound(self.explosion)
        elif self.pos_y > SH - self.rad:
            self.dy = 0
            self.pos_y = SH - self.rad
            arcade.play_sound(self.explosion)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.box = Box(50, 50, 0, 0, 30, arcade.color.AUBURN)
        self.box2 = Box(SW-50, SH-50, 0, 0, 30, arcade.color.DUKE_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.box.draw()
        self.box2.draw()

    def on_update(self, dt):

        if self.box2.pos_y + self.box.rad == self.box.pos_y + self.box.rad:
            self.box2.dy = 0
            self.box2.pos_y = self.box.pos_y + self.box2.rad
        elif self.box2.pos_y - self.box.rad == self.box.pos_y - self.box.rad:
            self.box.dy = 0
            self.box.pos_y = self.box2.pos_y + self.box.rad
        elif self.box2.pos_x + self.box.rad == self.box.pos_x + self.box.rad:
            self.box2.dx = 0
            self.box2.pos_x = self.box.pos_x - self.box2.rad
        elif self.box2.pos_x - self.box.rad == self.box.pos_x - self.box.rad:
            self.box.dx = 0
            self.box.pos_x = self.box2.pos_x - self.box.rad
        else:
            self.box.update()
            self.box2.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.box.dx = -SPEED1
        elif key == arcade.key.RIGHT:
            self.box.dx = SPEED1
        elif key == arcade.key.UP:
            self.box.dy = SPEED1
        elif key == arcade.key.DOWN:
            self.box.dy = -SPEED1
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
            self.box.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.box.dy = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.box2.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.box2.dy = 0

def main():
    window = MyGame(SW, SH, "Jedi Training")
    arcade.run()

if __name__=="__main__":
    main()