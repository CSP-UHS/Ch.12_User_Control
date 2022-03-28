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
Navigate to the end of the maze

'''
import arcade
SW = 640
SH = 480
SPEED = 5   # 3 x 60 = 180 pixels/second

class Ball:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.explosion = arcade.load_sound("Sounds/explosion.mp3")
        self.laser = arcade.load_sound("Sounds/laser.mp3")

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update(self):
        self.pos_y += self.dy
        self.pos_x += self.dx
        if self.pos_x >= SW or self.pos_x <= 0:
            if self.pos_x > 250:
                self.pos_x -= 30
            elif self.pos_x < 250:
                self.pos_x += 30
        if self.pos_y >= SH or self.pos_y <= 0:
            if self.pos_y > 250:
                self.pos_y -= 30
                arcade.close_window()
                print("YOU WIN!")
            elif self.pos_y < 250:
                self.pos_y += 30
        if self.pos_x <= 450 and self.pos_x >= 400 and self.dx >= 1:
            if self.pos_y >= 380:
                self.pos_x = 460
                self.pos_y = 75
        if self.pos_x <= 450 and self.pos_x >= 400 and self.dx <= 0:
            if self.pos_y >= 380:
                self.pos_x = 390
                self.pos_y = 75
        if self.pos_x <= 450 and self.pos_x >= 400 and self.dx >= 1:
            if self.pos_y <= 100:
                self.pos_x = 460
                self.pos_y = 405
        if self.pos_x <= 450 and self.pos_x >= 400 and self.dx <= 0:
            if self.pos_y <= 100:
                self.pos_x = 390
                self.pos_y = 405
        if self.pos_x <= 50:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x >= 175 and self.pos_x <= 225 and self.pos_y >= 100 and self.pos_y <= 350:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x <= 175 and self.pos_x >= 100 and self.pos_y >= 300 and self.pos_y <= 350:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_y <= 50:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x <= 175 and self.pos_x >= 50 and self.pos_y >= 100 and self.pos_y <= 150:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_y >= 430 and self.pos_x <= 590:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x <= 300 and self.pos_x >= 225 and self.pos_y >= 150 and self.pos_y <= 200:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x <= 350 and self.pos_x >= 300 and self.pos_y >= 100 and self.pos_y <= 150:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_y >= 250 and self.pos_y <=300 and self.pos_x <=400 and self.pos_x >= 275:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x <= 450 and self.pos_x >= 400 and self.pos_y >= 100 and self.pos_y <= 380:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x <= 550 and self.pos_x >= 500 and self.pos_y >= 50 and self.pos_y <= 250:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x <= 590 and self.pos_x >= 540 and self.pos_y >= 380 and self.pos_y <= 430:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)
        if self.pos_x <= 590 and self.pos_x >= 450 and self.pos_y <= 380 and self.pos_y >= 330:
            arcade.play_sound(self.explosion)
            arcade.close_window()
            print("YOU DIED!")
            arcade.play_sound(self.explosion)




class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.LIGHT_STEEL_BLUE)
        self.x = input(str("Invisible? y/n"))
        self.explosion = arcade.load_sound("Sounds/explosion.mp3")
        self.laser = arcade.load_sound("Sounds/laser.mp3")

        x2 = 75
        y2 = 75
        dx = 0
        dy = 0
        r = 15
        c = arcade.color.YELLOW
        self.ball = Ball(x2, y2, dx, dy, r, c)


    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        if self.x == "n" or self.x=="N":
            arcade.draw_lrtb_rectangle_filled(0, 50, 480, 0, arcade.color.ROSE)
            arcade.draw_lrtb_rectangle_filled(50, 175, 150, 100, arcade.color.ROSE_GOLD)
            arcade.draw_lrtb_rectangle_filled(50, 640, 50, 0, arcade.color.AMERICAN_ROSE)
            arcade.draw_lrtb_rectangle_filled(50, 590, 480, 430, arcade.color.RED_VIOLET)
            arcade.draw_lrtb_rectangle_filled(175, 225, 350, 100, arcade.color.BLUEBONNET)
            arcade.draw_lrtb_rectangle_filled(100, 175, 350, 300, arcade.color.BLUE_GREEN)
            arcade.draw_lrtb_rectangle_filled(225, 300, 200, 150, arcade.color.DIM_GRAY)
            arcade.draw_lrtb_rectangle_filled(300, 350, 200, 100, arcade.color.PURPLE_HEART)
            arcade.draw_lrtb_rectangle_filled(400, 450, 380, 100, arcade.color.BUD_GREEN)
            arcade.draw_lrtb_rectangle_filled(275, 400, 300, 250, arcade.color.GUPPIE_GREEN)
            arcade.draw_lrtb_rectangle_filled(400, 450, 430, 380, arcade.color.ORANGE)
            arcade.draw_lrtb_rectangle_filled(400, 450, 100, 50, arcade.color.BLUE)
            arcade.draw_lrtb_rectangle_filled(450, 590, 380, 330, arcade.color.ORIOLES_ORANGE)
            arcade.draw_lrtb_rectangle_filled(540, 590, 430, 380, arcade.color.BOSTON_UNIVERSITY_RED)
            arcade.draw_lrtb_rectangle_filled(500, 550, 250, 50, arcade.color.YELLOW_ROSE)



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
        elif key == arcade.key.L:
            arcade.play_sound(self.explosion)
        elif key == arcade.key.K:
            arcade.play_sound(self.laser)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0

def main():
    window = MyGame(SW, SH, "Tunnel")
    arcade.run()

if __name__=="__main__":
    main()