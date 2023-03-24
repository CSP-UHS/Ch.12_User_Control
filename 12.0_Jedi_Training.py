'''
Sign your name: Tanner Evitts
 
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
SW = 500
SH = 500
SPEED1 = 3
SPEED2 = 4


class Box():
    def __init__(self,name,pos_x,pos_y,dx,dy,l,col):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.l = l
        self.col = col
        self.laser_sound = arcade.load_sound("laser.wav")
        self.explosion_sound = arcade.load_sound("explosion.wav")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.l, self.l, self.col)

    def update_box(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
        if self.pos_x < (self.l/2) and self.name == "BlueBox":
            self.pos_x = (self.l/2)
            arcade.play_sound(self.laser_sound)
        if self.pos_x < (self.l/2) and self.name == "RedBox":
            self.pos_x = (self.l/2)
            arcade.play_sound(self.explosion_sound)
        if self.pos_y < (self.l/2) and self.name == "BlueBox":
            self.pos_y = (self.l/2)
            arcade.play_sound(self.laser_sound)
        if self.pos_y < (self.l/2) and self.name == "RedBox":
            self.pos_y = (self.l/2)
            arcade.play_sound(self.explosion_sound)
        if self.pos_x > SW - (self.l/2) and self.name == "BlueBox":
            self.pos_x = SW - (self.l/2)
            arcade.play_sound(self.laser_sound)
        if self.pos_x > SW - (self.l/2) and self.name == "RedBox":
            self.pos_x = SW - (self.l/2)
            arcade.play_sound(self.explosion_sound)
        if self.pos_y > SH - (self.l/2) and self.name == "BlueBox":
            self.pos_y = SH - (self.l/2)
            arcade.play_sound(self.laser_sound)
        if self.pos_y > SH - (self.l/2) and self.name == "RedBox":
            self.pos_y = SH - (self.l/2)
            arcade.play_sound(self.explosion_sound)

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.blueBox = Box("BlueBox",50, 50, 0, 0, 30, arcade.color.BLUE)
        self.redBox = Box("RedBox",450, 450, 0, 0 , 30, arcade.color.RED)
        self.set_mouse_visible(False)
        # self.balllist = []
        # for i in range(30):
        #     pos_x = random.randint(20,620)
        #     pos_y = random.randint(20,460)
        #     dx = random.randint(1,3)
        #     dy = random.randint(1,3)
        #     rad = random.randint(7,30)
        #     col = color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
        #     self.ball = Ball(pos_x,pos_y,dx,dy,rad,col)
        #     self.balllist.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        self.redBox.draw_box()
        self.blueBox.draw_box()
        # for item in self.balllist:
        #     item.draw_ball()


    def on_update(self,dt):
        self.redBox.update_box()
        self.blueBox.update_box()
    #     for item in self.balllist:
    #         item.update_ball()
    def on_key_press(self,key,modifiers):
        if key == arcade.key.LEFT:
            self.redBox.dx = -SPEED1
        elif key == arcade.key.RIGHT:
            self.redBox.dx = SPEED1
        elif key == arcade.key.UP:
            self.redBox.dy = SPEED1
        elif key == arcade.key.DOWN:
            self.redBox.dy = -SPEED1
        if key == arcade.key.A:
            self.blueBox.dx = -SPEED2
        elif key == arcade.key.D:
            self.blueBox.dx = SPEED2
        elif key == arcade.key.W:
            self.blueBox.dy = SPEED2
        elif key == arcade.key.S:
            self.blueBox.dy = -SPEED2

    def on_key_release(self,key,modifiers):
        if key == arcade.key.LEFT:
            self.redBox.dx = 0
        elif key == arcade.key.RIGHT:
            self.redBox.dx = 0
        elif key == arcade.key.UP:
            self.redBox.dy = 0
        elif key == arcade.key.DOWN:
            self.redBox.dy = 0
        if key == arcade.key.A:
            self.blueBox.dx = 0
        elif key == arcade.key.D:
            self.blueBox.dx = 0
        elif key == arcade.key.W:
            self.blueBox.dy = 0
        elif key == arcade.key.S:
            self.blueBox.dy = 0

    # def on_mouse_motion(self,x,y,dx,dy):
    #     self.ball.pos_x = x
    #     self.ball.pos_y = y
    #
    # def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
    #     if button == arcade.MOUSE_BUTTON_LEFT:
    #         print("Left Mouse button pressed at (",x,",",y,")")
    #     elif button == arcade.MOUSE_BUTTON_RIGHT:
    #         print("Right Mouse button pressed at (",x,",",y,")")

def main():
    window=MyGame(SW,SH,"User Control")
    arcade.run()

if __name__ == "__main__":
    main()