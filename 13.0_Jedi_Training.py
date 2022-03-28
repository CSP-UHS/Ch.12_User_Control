'''
Sign your name:________________
 
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
import random
SW=500
SH=500
blue_speed=4
red_speed=3
green_speed=3.5
orange_speed=4.25
class Red_box:

    def __init__(self, pos_x, pos_y, dx, dy, s, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.s = s

        self.col = col

        self.dx = dx

        self.dy = dy

        self.laser = arcade.load_sound("sounds/laser.mp3")

        self.explosion = arcade.load_sound("sounds/explosion.mp3")




    def draw(self):

        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.s,self.s,self.col)

    def update(self):

        self.pos_x += self.dx

        self.pos_y += self.dy


        if self.pos_x < self.s/2:
            self.dx=0
            self.pos_x=self.s/2
            arcade.play_sound(self.laser,3.0)
        elif self.pos_x > SW-self.s/2:
            self.dx=0
            self.pos_x=SW-self.s/2
            arcade.play_sound(self.explosion,3.0)
        elif self.pos_y<self.s/2:
            self.dy=0
            self.pos_y=self.s/2
            arcade.play_sound(self.laser,3.0)
        elif self.pos_y>SH-self.s/2:
            self.dy=0
            self.pos_y=SH-self.s/2
            arcade.play_sound(self.explosion,3.0)




class Blue_box:

    def __init__(self, pos_x, pos_y, dx, dy, s, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.s = s

        self.col = col

        self.dx = dx

        self.dy = dy

        self.laser = arcade.load_sound("sounds/laser.mp3")

        self.explosion = arcade.load_sound("sounds/explosion.mp3")



    def draw(self):

        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.s,self.s,self.col)

    def update(self):

        self.pos_x += self.dx

        self.pos_y += self.dy

        if self.pos_x < self.s/2:
            self.dx=0
            self.pos_x=self.s/2
            arcade.play_sound(self.laser,3)
        elif self.pos_x > SW-self.s/2:
            self.dx=0
            self.pos_x=SW-self.s/2
            arcade.play_sound(self.explosion,3)
        elif self.pos_y < self.s/2:
            self.dy=0
            self.pos_y=self.s/2
            arcade.play_sound(self.laser,3)
        elif self.pos_y > SH-self.s/2:
            self.dy=0
            self.pos_y=SH-self.s/2
            arcade.play_sound(self.explosion,3)


class Green_box:

    def __init__(self, pos_x, pos_y, dx, dy, s, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.s = s

        self.col = col

        self.dx = dx

        self.dy = dy

        self.laser = arcade.load_sound("sounds/laser.mp3")

        self.explosion = arcade.load_sound("sounds/explosion.mp3")



    def draw(self):

        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.s,self.s,self.col)

    def update(self):

        self.pos_x += self.dx

        self.pos_y += self.dy

        if self.pos_x < self.s/2:
            self.dx=0
            self.pos_x=self.s/2
            arcade.play_sound(self.laser,3)
        elif self.pos_x > SW-self.s/2:
            self.dx=0
            self.pos_x=SW-self.s/2
            arcade.play_sound(self.explosion,3)
        elif self.pos_y < self.s/2:
            self.dy=0
            self.pos_y=self.s/2
            arcade.play_sound(self.laser,3)
        elif self.pos_y > SH-self.s/2:
            self.dy=0
            self.pos_y=SH-self.s/2
            arcade.play_sound(self.explosion,3)


class Orange_box:

    def __init__(self, pos_x, pos_y, dx, dy, s, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.s = s

        self.col = col

        self.dx = dx

        self.dy = dy

        self.laser = arcade.load_sound("sounds/laser.mp3")

        self.explosion = arcade.load_sound("sounds/explosion.mp3")



    def draw(self):

        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.s,self.s,self.col)

    def update(self):

        self.pos_x += self.dx

        self.pos_y += self.dy

        if self.pos_x < self.s/2:
            self.dx=0
            self.pos_x=self.s/2
            arcade.play_sound(self.laser,3)
        elif self.pos_x > SW-self.s/2:
            self.dx=0
            self.pos_x=SW-self.s/2
            arcade.play_sound(self.explosion,3)
        elif self.pos_y < self.s/2:
            self.dy=0
            self.pos_y=self.s/2
            arcade.play_sound(self.laser,3)
        elif self.pos_y > SH-self.s/2:
            self.dy=0
            self.pos_y=SH-self.s/2
            arcade.play_sound(self.explosion,3)















class MyGame(arcade.Window):



    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.red_box = Red_box(SW/2, SH/2, 0, 0, 30, arcade.color.RED)

        self.blue_box = Blue_box(SW/3,SH/3, 0, 0, 30,arcade.color.BLUE)

        self.green_box = Green_box(SW/6, SH/6, 0, 0, 30, arcade.color.GREEN)

        self.orange_box = Orange_box(SW/4*3, SH/4*3, 0, 0, 30, arcade.color.ORANGE)




    def on_draw(self):

        arcade.start_render()

        self.red_box.draw()
        self.blue_box.draw()
        self.green_box.draw()
        self.orange_box.draw()

    def on_update(self, dt):

        self.red_box.update()

        self.blue_box.update()

        self.green_box.update()

        self.orange_box.update()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:

            self.blue_box.dx = -blue_speed

        elif key == arcade.key.RIGHT:

            self.blue_box.dx = blue_speed

        elif key == arcade.key.UP:

            self.blue_box.dy = blue_speed

        elif key == arcade.key.DOWN:

            self.blue_box.dy = -blue_speed

        elif key == arcade.key.W:

            self.red_box.dy = red_speed

        elif key == arcade.key.S:

            self.red_box.dy = -red_speed

        elif key == arcade.key.D:

            self.red_box.dx = red_speed

        elif key == arcade.key.A:

            self.red_box.dx = -red_speed

        elif key == arcade.key.I:

            self.green_box.dy = green_speed

        elif key == arcade.key.K:

            self.green_box.dy = -green_speed

        elif key == arcade.key.J:

            self.green_box.dx = -green_speed

        elif key == arcade.key.L:

            self.green_box.dx = green_speed

        elif key == arcade.key.H:

            self.orange_box.dx = orange_speed

        elif key == arcade.key.F:

            self.orange_box.dx = -orange_speed

        elif key == arcade.key.T:
            
            self.orange_box.dy = orange_speed

        elif key == arcade.key.G:

            self. orange_box.dy = -orange_speed

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:

            self.blue_box.dx = 0

        elif key == arcade.key.UP or key == arcade.key.DOWN:

            self.blue_box.dy = 0

        elif key == arcade.key.W or key == arcade.key.S:

            self.red_box.dy = 0

        elif key == arcade.key.D or key == arcade.key.A:

            self.red_box.dx = 0

        elif key == arcade.key.J or key == arcade.key.L:

            self.green_box.dx = 0

        elif key == arcade.key.I or key == arcade.key.K:

            self.green_box.dy = 0

        elif key == arcade.key.T or key == arcade.key.G:

            self.orange_box.dy = 0

        elif key == arcade.key.H or key == arcade.key.F:

            self.orange_box.dx = 0






def main():

    window = MyGame(SW, SH, "Hermonator Salvation")

    arcade.run()



if __name__=="__main__":

    main()



