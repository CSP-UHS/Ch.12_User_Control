import arcade
import random
SW = 640
SH = 480
SPEED1 = 3
SPEED2 = 2


class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.laser_sound = arcade.load_sound("laser.wav")

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)

    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
        if self.pos_x < self.rad:
            self.pos_x = self.rad
            arcade.play_sound(self.laser_sound)
        if self.pos_y < self.rad:
            self.pos_y = self.rad
        if self.pos_x > SW - self.rad:
            self.pos_x = SW - self.rad
        if self.pos_y > SH - self.rad:
            self.pos_y = SH - self.rad

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.BLACK)
        self.wasdball = Ball(590, 430, 0, 0 , 15, arcade.color.BLUE)
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
        self.ball.draw_ball()
        self.wasdball.draw_ball()
        # for item in self.balllist:
        #     item.draw_ball()


    def on_update(self,dt):
        self.ball.update_ball()
        self.wasdball.update_ball()
    #     for item in self.balllist:
    #         item.update_ball()
    def on_key_press(self,key,modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -SPEED1
        elif key == arcade.key.RIGHT:
            self.ball.dx = SPEED1
        elif key == arcade.key.UP:
            self.ball.dy = SPEED1
        elif key == arcade.key.DOWN:
            self.ball.dy = -SPEED1
        if key == arcade.key.A:
            self.wasdball.dx = -SPEED2
        elif key == arcade.key.D:
            self.wasdball.dx = SPEED2
        elif key == arcade.key.W:
            self.wasdball.dy = SPEED2
        elif key == arcade.key.S:
            self.wasdball.dy = -SPEED2

    def on_key_release(self,key,modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = 0
        elif key == arcade.key.RIGHT:
            self.ball.dx = 0
        elif key == arcade.key.UP:
            self.ball.dy = 0
        elif key == arcade.key.DOWN:
            self.ball.dy = 0
        if key == arcade.key.A:
            self.wasdball.dx = 0
        elif key == arcade.key.D:
            self.wasdball.dx = 0
        elif key == arcade.key.W:
            self.wasdball.dy = 0
        elif key == arcade.key.S:
            self.wasdball.dy = 0

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