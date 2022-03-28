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
SW=600
SH=600
SPEED=2
star=True
class Red_box:

    def __init__(self, pos_x, pos_y, dx, dy, s, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.s = s

        self.col = col

        self.dx = dx

        self.dy = dy

        self.laser = arcade.load_sound("sounds/laser.mp3")

        self.key_4= arcade.load_sound("sounds/key04.mp3")

        self.key_5 = arcade.load_sound("sounds/key05.mp3")

        self.key_6 = arcade.load_sound("sounds/key06.mp3")

        self.key_7 = arcade.load_sound("sounds/key07.mp3")

        self.key_8 = arcade.load_sound("sounds/key08.mp3")

        self.key_9 = arcade.load_sound("sounds/key09.mp3")

        self.key_10 = arcade.load_sound("sounds/key10.mp3")

        self.key_11 = arcade.load_sound("sounds/key11.mp3")

        self.key_12 = arcade.load_sound("sounds/key12.mp3")

        self.key_13 = arcade.load_sound("sounds/key13.mp3")

        self.key_14 = arcade.load_sound("sounds/key14.mp3")

        self.key_15 = arcade.load_sound("sounds/key15.mp3")

    def draw(self):
        arcade.draw_ellipse_filled(300,350,100,50,arcade.color.AUBURN)
        arcade.draw_triangle_filled(300,280,250,350,350,350,arcade.color.AUBURN)
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.s, self.s, self.col)
        arcade.draw_triangle_filled(300,350,320,400,280,400,arcade.color.ASH_GREY)



        arcade.draw_rectangle_filled(10,27,20,54,arcade.color.SALMON)
        arcade.draw_rectangle_filled(10,81,20,54,arcade.color.DEEP_PEACH)
        arcade.draw_rectangle_filled(10,135,20,54,arcade.color.GRAY)
        arcade.draw_rectangle_filled(10,189,20,54,arcade.color.LIGHT_GRAY)
        arcade.draw_rectangle_filled(10,241,20,54,arcade.color.BLUE_GRAY)
        arcade.draw_rectangle_filled(10,295,20,54,arcade.color.LIGHT_BLUE)
        arcade.draw_rectangle_filled(10,349,20,54,arcade.color.CARIBBEAN_GREEN)
        arcade.draw_rectangle_filled(10,403,20,54,arcade.color.BEIGE)
        arcade.draw_rectangle_filled(10,457,20,54,arcade.color.ASH_GREY)
        arcade.draw_rectangle_filled(10,511,20,54,arcade.color.WHITE)
        arcade.draw_rectangle_filled(10,569,20,62,arcade.color.ANDROID_GREEN)
        arcade.draw_text("Guy",500, 473.8, arcade.color.ASH_GREY, 12, 30, "center", "arial")
        arcade.draw_text("You're in",258,330, arcade.color.AUBURN, 12,70, "center", "arial")
        arcade.draw_text("Almost ready right?",258, 150, arcade.color.ASH_GREY,12, 300, "center", "arial")
        arcade.draw_text("Been ready man", 120, 120, arcade.color.ASH_GREY, 12, 300, "center", "arial")
        arcade.draw_text("Green", 267, 90, arcade.color.ASH_GREY, 12, 300, "center", "arial")
        arcade.draw_text("What?",500, 60, arcade.color.ASH_GREY, 12, 60, "center", "arial")
        arcade.draw_text("Hmm?", 150, 30, arcade.color.ASH_GREY, 12, 300, "center", "arial")
        arcade.draw_text("You said something", 300, 0, arcade.color.ASH_GREY,12,300, "center", "arial")





    def update(self):
        self.pos_x += self.dx

        self.pos_y += self.dy

        if self.pos_x<=0 and self.pos_y<=54:
            self.pos_x = self.s / 2
            arcade.play_sound(self.key_4,3.0)

        elif self.pos_x<=0 and self.pos_y<=108:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_5,3.0)
        elif self.pos_x<=0 and self.pos_y<=162:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_6,3.0)
        elif self.pos_x<=0 and self.pos_y<=216:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_7,3.0)
        elif self.pos_x<=0 and self.pos_y<=270:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_8)
        elif self.pos_x<=0 and self.pos_y<=324:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_9,3.0)
        elif self.pos_x<=0 and self.pos_y<=378:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_10,3.0)
        elif self.pos_x<=0 and self.pos_y<=432:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_11,3.0)
        elif self.pos_x<=0 and self.pos_y<=486:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_12,3.0)
        elif self.pos_x<=0 and self.pos_y<=540:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_13,3.0)
        elif self.pos_x<=0 and self.pos_y<=600:
            self.pos_x = self.s/2
            arcade.play_sound(self.key_14,3.0)
        elif self.pos_x > SW - self.s / 2:
            self.dx = 0
            self.pos_x = SW - self.s / 2
            arcade.play_sound(self.laser, 3.0)
        elif self.pos_y < self.s / 2:
            self.dy = 0
            self.pos_y = self.s / 2
            arcade.play_sound(self.laser, 3.0)
        elif self.pos_y > SH - self.s / 2:
            self.dy = 0
            self.pos_y = SH - self.s / 2
            arcade.play_sound(self.laser, 3.0)
        elif self.pos_x<=20+self.s/2 and self.pos_y<=54:
            self.col=arcade.color.SALMON
        elif self.pos_x<=20+self.s/2 and self.pos_y<=108 and self.pos_y>54:
            self.col=arcade.color.DEEP_PEACH
        elif self.pos_x<=20+self.s/2 and self.pos_y<=162 and self.pos_y>108:
            self.col=arcade.color.GRAY
        elif self.pos_x<=20+self.s/2 and self.pos_y<=216 and self.pos_y>162:
            self.col=arcade.color.LIGHT_GRAY
        elif self.pos_x<=20+self.s/2 and self.pos_y<=270 and self.pos_y>216:
            self.col=arcade.color.BLUE_GRAY
        elif self.pos_x<=20+self.s/2 and self.pos_y<=324 and self.pos_y>270:
            self.col=arcade.color.LIGHT_BLUE
        elif self.pos_x<=20+self.s/2 and self.pos_y<=378 and self.pos_y>324:
            self.col=arcade.color.CARIBBEAN_GREEN
        elif self.pos_x<=20+self.s/2 and self.pos_y<=432 and self.pos_y>378:
            self.col=arcade.color.BEIGE
        elif self.pos_x<=20+self.s/2 and self.pos_y<=486 and self.pos_y>432:
            self.col=arcade.color.ASH_GREY
        elif self.pos_x<=20+self.s/2 and self.pos_y<=540 and self.pos_y>486:
            self.col=arcade.color.WHITE
        elif self.pos_x<=20+self.s/2 and self.pos_y<=600 and self.pos_y>540:
            self.col=arcade.color.ANDROID_GREEN





class MyGame(arcade.Window):



    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.red_box = Red_box(50, 50, 0, 0, 30, arcade.color.BLUE_YONDER)



    def on_draw(self):

        arcade.start_render()

        self.red_box.draw()



    def on_update(self, dt):

        self.red_box.update()




    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:

            self.red_box.dx = -SPEED

        elif key == arcade.key.RIGHT:

            self.red_box.dx = SPEED

        elif key == arcade.key.UP:

            self.red_box.dy = SPEED

        elif key == arcade.key.DOWN:

            self.red_box.dy = -SPEED



    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:

            self.red_box.dx = 0

        elif key == arcade.key.UP or key == arcade.key.DOWN:

            self.red_box.dy = 0


def main():

    window = MyGame(SW, SH, "Key Press Example")

    arcade.run()



if __name__=="__main__":

    main()