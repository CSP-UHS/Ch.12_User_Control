import arcade



SW = 640

SH = 480



class Ball:

    def __init__(self, pos_x, pos_y, rad, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.rad = rad

        self.col = col



    def draw(self):

        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)





class MyGame(arcade.Window):



    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)



    def on_draw(self):

        arcade.start_render()

        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.pos_x = x

        self.ball.pos_y = y





def main():

    window = MyGame(SW, SH, "Mouse Example")

    arcade.run()



if __name__=="__main__":

    main()