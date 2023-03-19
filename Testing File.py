import arcade
import random
SW = 640
SH = 480
SPEED = 3

class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.laser = arcade.load_sound("laser.wav")
        self.explosion = arcade.load_sound("explosion.wav")
        # self.call = arcade.load_sound("Answer-11.wav")
    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y ,self.rad,self.col)

    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy

    #bounce ball off edge of screens

        if self.pos_x < self.rad:
            self.pos_x = self.rad
            arcade.play_sound(self.laser)
        elif self.pos_x > SW - self.rad:
            self.pos_x = SW - self.rad
            arcade.play_sound(self.laser)
        elif self.pos_y < self.rad:
            self.pos_y = self.rad
            arcade.play_sound(self.explosion)
        elif self.pos_y > SH - self.rad:
            self.pos_y = SH - self.rad
            arcade.play_sound(self.explosion)






class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.ball1 = Ball(50,50,0,0,15,arcade.color.BLUE)

        self.ball2 = Ball (SW-50,SH-50,0,0,15,arcade.color.RED)
        self.set_mouse_visible(False)
        # self.ball_list=[]
        # for i in range(100):
        #     r=random.randint(10,30)
        #     x=random.randint(r,SW-r)
        #     y=random.randint(r,SH-r)
        #     vx=random.randint(-3,3)
        #     vy=random.randint(-3,3)
        #     c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #     if vx ==0:
        #         vx = random.randint(1,3)
        #     if vy ==0:
        #         vy = random.randint(-3,-1)
        #     self.ball = Ball(x,y,vx,vy,r,c)
        #     self.ball_list.append(self.ball)


    def on_draw(self):
        arcade.start_render()
        self.ball1.draw_ball()
        self.ball2.draw_ball()

    def on_update(self,dt):
        self.ball1.update_ball()
        self.ball2.update_ball()

    # def on_mouse_motion(self,x,y,dx,dy):
    #     self.ball.pos_x = x
    #     self.ball.pos_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball1.dx = -SPEED-1
        elif key == arcade.key.RIGHT:
            self.ball1.dx = SPEED+1
        elif key == arcade.key.UP:
            self.ball1.dy = SPEED+1
        elif key == arcade.key.DOWN:
            self.ball1.dy = -SPEED-1

        if key == arcade.key.A:
            self.ball2.dx = -SPEED
        elif key == arcade.key.D:
            self.ball2.dx = SPEED
        elif key == arcade.key.W:
            self.ball2.dy = SPEED
        elif key == arcade.key.S:
            self.ball2.dy = -SPEED
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball1.dx = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball1.dy = 0

        if key == arcade.key.A or key == arcade.key.D:
            self.ball2.dx = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.ball2.dy = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left Mouse Button Pressed at", x,y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right Mouse Button Pressed at", x,y)

def main():
    window = MyGame(SW,SH,"Drawing Example")
    arcade.run()
if __name__ == "__main__":
    main()