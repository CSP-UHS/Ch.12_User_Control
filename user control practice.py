import arcade

SW = 640
SH = 480
SPEED = 3    # 3 x 60 = 180 pixels/second

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
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

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
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

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
    window = MyGame(SW, SH, "Key Press Example")
    arcade.run()

if __name__=="__main__":
    main()