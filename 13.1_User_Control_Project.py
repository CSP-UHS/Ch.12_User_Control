

import arcade
import time

SW = 500
SH = 500


class Box():
    def __init__(self, x, y, speed, r, c, CS, x2,y2, s2,r2,c2,CS2):
        self.x = x
        self.y = y
        self.speed = speed
        self.r = r
        self.color = c
        self.CS = CS
        self.dx = 0
        self.dy = 0
        self.x2 = x2
        self.y2 = y2
        self.s2 = s2
        self.r2 = r2
        self.c2 = c2
        self.CS2 = CS2
        self.dx2 = 0
        self.dy2 = 0
        if c == arcade.color.BLUE:
            self.wallhit = arcade.load_sound("laser.mp3")

        self.wall = arcade.load_sound("explosion.mp3")

    def control(self, key):
        # print(key)
        if self.CS2 == "wasd":
            if key == 119:
                self.dy2 = self.s2
            if key == 97:
                self.dx2 = -self.s2
            if key == 115:
                self.dy2 = -self.s2
            if key == 100:
                self.dx2 = self.s2

        if self.CS == "arrows":
            if key == 65362:
                self.dy = self.speed
            if key == 65361:
                self.dx = -self.speed
            if key == 65364:
                self.dy = -self.speed
            if key == 65363:
                self.dx = self.speed

    def stop(self, key):
        # print(key)
        if self.CS2 == "wasd":
            if key == 119:
                self.dy2 = 0
            if key == 97:
                self.dx2 = 0
            if key == 115:
                self.dy2 = 0
            if key == 100:
                self.dx2 = 0

        if self.CS == "arrows":
            if key == 65362:
                self.dy = 0
            if key == 65361:
                self.dx = 0
            if key == 65364:
                self.dy = 0
            if key == 65363:
                self.dx = 0

    def drawbox(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.r, self.r, self.color)
        arcade.draw_rectangle_filled(self.x2,self.y2,self.r2,self.r2,self.c2)

    def updatebox(self):

        self.x += self.dx
        self.y += self.dy
        self.x2 += self.dx2
        self.y2 += self.dy2

        if self.x > (500 - self.r * 0.5):
            self.x = 500 - self.r * 0.5
            self.dx = 0
        if self.x > 90 and self.x < 110 and self.CS =="arrows" and self.y < 160:
            self.dx = 0
            arcade.play_sound(self.wallhit, 1)
            time.sleep(.5)
            arcade.close_window()
        if self.x > 140 and self.x < 160 and self.CS =="arrows" and self.y > 290:
            self.dx = 0
            arcade.play_sound(self.wallhit, 1)
            time.sleep(.5)
            arcade.close_window()
        if self.x > 220 and self.x < 240 and self.CS =="arrows" and self.y < 280 and self.y > 220:
            self.dx = 0
            arcade.play_sound(self.wallhit, 1)
            time.sleep(.5)
            arcade.close_window()
        if self.x > 220 and self.x < 280 and self.CS =="arrows" and self.y < 280 and self.y > 260:
            self.dx = 0
            arcade.play_sound(self.wallhit, 1)
            time.sleep(.5)
            arcade.close_window()
        if self.x > 260 and self.x < 280 and self.CS =="arrows" and self.y < 280 and self.y > 220:
            self.dx = 0
            arcade.play_sound(self.wallhit, 1)
            time.sleep(.5)
            arcade.close_window()
        if self.x > 220 and self.x < 280 and self.CS =="arrows" and self.y < 240 and self.y > 220:
            self.dx = 0
            arcade.play_sound(self.wallhit, 1)
            time.sleep(.5)
            arcade.close_window()
        if self.x > 390 and self.CS =="arrows" and self.y < 110 and self.y > 90:
            self.dx = 0
            arcade.play_sound(self.wallhit, 1)
            time.sleep(.5)
            arcade.close_window()
        if self.x < self.x2 + 30 and self.x > self.x2 - 30 and self.y < self.y2 + 30 and self.y > self.y2 - 30:
            self.dx = 0
            self.dy = 0
            arcade.play_sound(self.wall, 1)
            time.sleep(.5)
            arcade.close_window()
        #if self.y < self.y2 + 10 and self.y > self.y2 - 10:
            #self.dx = 0
            #self.dy = 0
            #arcade.play_sound(self.wall, 1)
            #time.sleep(.5)
            #arcade.close_window()


        if self.y > (500 - self.r * 0.5):
            self.y = 500 - self.r * 0.5
            self.dy = 0
        if self.y < (0 + self.r * 0.5):
            self.y = 0 + self.r * 0.5
            self.dy = 0
        if self.x < (0 + self.r * 0.5):
            self.x = 0 + self.r * 0.5
            self.dx = 0

        if self.y2 > 480:
            self.y2 = 480
            self.dy2 = 0
        if self.y2 < 20:
            self.y2 = 20
            self.dy2 = 0
        if self.x2 > 480:
            self.x2 = 480
            self.dx2 = 0
        if self.x2 < 20:
            self.x2 = 20
            self.dx2 = 0

class Line():
    def __init__(self, start_x, start_y, end_x, end_y, color, width):
        self.sx = start_x
        self.sy = start_y
        self.ex = end_x
        self.ey = end_y
        self.color = color
        self.width = width
    def draw_line(self):
        arcade.draw_line(self.sx,self.sy,self.ex,self.ey,self.color,self.width)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.YELLOW)
        self.line_list = []
        line1 = Line(100,0,100,150,arcade.color.BLACK, 10)
        self.line_list.append(line1)
        line2 = Line(150,500,150,300,[0,0,0],10)
        self.line_list.append(line2)
        line3 = Line(230,230,230,270,[0,0,0],10)
        self.line_list.append(line3)
        line4 = Line(230,270,270,270,[0,0,0],10)
        self.line_list.append(line4)
        line5 = Line(270,270,270,230,[0,0,0],10)
        self.line_list.append(line5)
        line6 = Line(230,230,270,230,[0,0,0],10)
        self.line_list.append(line6)
        line7 = Line(500,100,400,100,[0,0,0],10)
        self.line_list.append(line7)

        self.box_list = []
        box1 = Box(0, 0, 10, 30, arcade.color.BLUE, "arrows",500,500,1,40,arcade.color.PURPLE,"wasd")
        self.box_list.append(box1)
        #box2 = Box(500,500,1,40,arcade.color.PURPLE,"wasd")
        #self.box_list.append(box2)


    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.drawbox()
        for line in self.line_list:
            line.draw_line()

    def on_update(self, dt):
        for box in self.box_list:
            box.updatebox()
    def on_key_press(self, symbol, modifiers: int):
        for box in self.box_list:
            box.control(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        print(symbol)
        for box in self.box_list:
            box.stop(symbol)


def main():
    mywindow = MyGame(SW, SH, "User Control Project")
    arcade.run()


if __name__ == "__main__":
    main()