
import arcade
import time
import sys

SW = 800
SH = 600
SPEED = 2.45

class Box():
    def __init__(self, pos_x, pos_y, dx, dy, wid, hei, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.wid = wid
        self.hei = hei
        self.col = col
        self.buzzer_sound = arcade.load_sound("Sounds/Buzzer Sound Effect.mp3")
        self.explosion_sound = arcade.load_sound("Sounds/explosion.mp3")


    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.wid, self.hei, self.col)
        arcade.draw_rectangle_outline(self.pos_x, self.pos_y, self.wid, self.hei, arcade.color.BLACK, 2)

    def update(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_y > SH - (self.hei/2):
            self.pos_y = SH - (self.hei/2)
        elif self.pos_y < 0 + (self.hei/2):
            self.pos_y = 0 + (self.hei/2)


class Ball():
    def __init__(self, pos_x, pos_y, dx, dy, rad, col, scoreL, scoreR):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.scoreL = scoreL
        self.scoreR = scoreR
        self.explosion_sound = arcade.load_sound("Sounds/explosion.mp3")
        self.buzzer_sound = arcade.load_sound("Sounds/Buzzer Sound Effect.mp3")
        self.border_bounce = arcade.load_sound("Sounds/phaseJump3.mp3")



    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)
        arcade.draw_circle_outline(self.pos_x, self.pos_y, self.rad, arcade.color.BLACK, 2)

    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        #MISS

            #RIGHT
        if self.pos_x > SW-self.rad:
            arcade.play_sound(self.buzzer_sound)
            time.sleep(2)
            self.dx *= -1
            self.dy *= -1
            self.pos_x = 650


            #LEFT
        elif self.pos_x < self.rad:
            arcade.play_sound(self.buzzer_sound)
            time.sleep(2)
            self.dx *= -1
            self.dy *= -1
            self.pos_x = 150


        #TOP AND BOTTOM BOUNCE
        if self.pos_y > SH - self.rad or self.pos_y < 0 + self.rad:
            arcade.play_sound(self.border_bounce)
            self.dy *= -1

        #SCORE
            #left score
        if self.pos_x > 786.65:
            self.scoreL += 1

        if self.pos_x < 14.35:
            self.scoreR += 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
        self.explosion_sound = arcade.load_sound("Sounds/Buzzer Sound Effect.mp3")
        self.border_bounce = arcade.load_sound("Sounds/phaseJump3.mp3")
        self.paddle_bounce = arcade.load_sound("Sounds/phaserUp2.mp3")
        self.victory = arcade.load_sound("Sounds/victory.mp3")
        self.box1 = Box(50, 75, 0, 0, 20, 100, arcade.color.SPANISH_RED)
        self.box2 = Box(750, 75, 0, 0, 20, 100, arcade.color.SPANISH_RED)
        self.ball = Ball(200, 300, 3.5, 3.5, 10, arcade.color.WHITE, 0, 0)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("PONG", 300, 500, arcade.color.BLACK, 50, 200, "center")
        arcade.draw_text("PONG", 304, 502, arcade.color.SPANISH_RED, 50, 200, "center")
        arcade.draw_text("UP and DOWN for RIGHT Paddle", 250, 420, arcade.color.BLACK, 11, 300, "center")
        arcade.draw_text("W and S for LEFT Paddle", 250, 400, arcade.color.BLACK, 11, 300, "center")
        arcade.draw_text("IF YOU SCORE MORE THAN 5 YOU WIN!", 250, 445, arcade.color.BLACK, 12, 300, "center", 'Calibri', True)
        arcade.draw_text("DONT LET THE BALL HIT YOUR WALL!", 240, 475, arcade.color.RED_DEVIL, 14, 320, "center")
        arcade.draw_text("SCORE", 200, 100, arcade.color.BLACK, 22, 400, "center")
        arcade.draw_text("SCORE", 202, 102, arcade.color.SPANISH_RED, 22, 400, "center")



        #SCOREBOARD BOXES:
        arcade.draw_rectangle_outline(366, 65, 60, 60, arcade.color.BLACK, 4)
        arcade.draw_rectangle_outline(368, 67, 60, 60, arcade.color.VENETIAN_RED, 4)


        arcade.draw_rectangle_outline(436, 65, 60, 60, arcade.color.BLACK, 4)
        arcade.draw_rectangle_outline(438, 67, 60, 60, arcade.color.VENETIAN_RED, 4)

        # SCOREBOARD LEFT
        if self.ball.scoreL == 0:
            arcade.draw_text("0", 167, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("0", 169, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreL == 1:
            arcade.draw_text("1", 167, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("1", 169, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreL == 2:
            arcade.draw_text("2", 167, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("2", 169, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreL == 3:
            arcade.draw_text("3", 167, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("3", 169, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreL == 4:
            arcade.draw_text("4", 167, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("4", 169, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreL == 5:
            arcade.draw_text("5", 167, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("5", 169, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreL == 6:
            arcade.draw_text("6", 167, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("6", 169, 34, arcade.color.SPANISH_RED, 45, 400, "center")
            arcade.play_sound(self.victory)
            time.sleep(3)
            sys.exit()





        # SCOREBOARD RIGHT
        if self.ball.scoreR == 0:
            arcade.draw_text("0", 237, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("0", 239, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreR == 1:
            arcade.draw_text("1", 237, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("1", 239, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreR == 2:
            arcade.draw_text("2", 237, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("2", 239, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreR == 3:
            arcade.draw_text("3", 237, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("3", 239, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreR == 4:
            arcade.draw_text("4", 237, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("4", 239, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreR == 5:
            arcade.draw_text("5", 237, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("5", 239, 34, arcade.color.SPANISH_RED, 45, 400, "center")
        elif self.ball.scoreR == 6:
            arcade.draw_text("6", 237, 32, arcade.color.BLACK, 45, 400, "center")
            arcade.draw_text("6", 239, 34, arcade.color.SPANISH_RED, 45, 400, "center")
            arcade.play_sound(self.victory)
            time.sleep(3)
            sys.exit()


        self.box1.draw()
        self.box2.draw()
        self.ball.draw_ball()


    def on_update(self, dt):
        self.box1.update()
        self.box2.update()
        self.ball.update_ball()
        print(self.ball.scoreL, self.ball.scoreR)



#BALL COLLISIONS

        #RIGHT PADDLE COLLISION
        if self.ball.pos_x > 730 and (self.ball.pos_y < self.box2.pos_y + 40 and self.ball.pos_y > self.box2.pos_y -40):
            arcade.play_sound(self.paddle_bounce)
            self.ball.dx *= -1

        #LEFT PADDLE COLLISION
        if self.ball.pos_x < 70 and (self.ball.pos_y < self.box1.pos_y +40 and self.ball.pos_y> self.box1.pos_y -40):
            arcade.play_sound(self.paddle_bounce)
            self.ball.dx *= -1



    def on_key_press(self, key, modifiers):
        #LEFT PADDLE
        if key == arcade.key.W:
            self.box1.dy = SPEED

        elif key == arcade.key.S:
            self.box1.dy = -SPEED

        #RIGHT PADDLE
        if key == arcade.key.UP:
            self.box2.dy = SPEED

        elif key == arcade.key.DOWN:
            self.box2.dy = -SPEED



    def on_key_release(self, key, modifiers):
        #LEFT PADDLE
        if key == arcade.key.W or key == arcade.key.S:
            self.box1.dy = 0




        #RIGHT PADDLE
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.box2.dy = 0



def main():
    window = MyGame(SW, SH, "PONG")
    arcade.run()




if __name__=="__main__":
    main()
