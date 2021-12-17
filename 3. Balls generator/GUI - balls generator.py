from tkinter import *
from random import randint

WIDTH = 1000
HEIGHT = 1000


class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, x+diameter, y+diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coords = self.canvas.coords(self.image)
        if coords[2] >= self.canvas.winfo_width() or coords[0] <= 0:
            self.xVelocity = -self.xVelocity
        if coords[3] >= self.canvas.winfo_height() or coords[1] <= 0:
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)


def gen_speed():
    return randint(1, 10)


def gen_size():
    return randint(10, 299)


def gen_coords():
    return randint(300, 699)


def gen_color():
    return ('#%06X' % randint(0, 0xFFFFFF))


def generate_balls():
    number = 'x'
    balls = []
    while number.isdigit() is False:
        number = input('How many balls do you want?: ')
    for i in range(int(number)):
        i = Ball(canvas, gen_coords(), gen_coords(), gen_size(), gen_speed(), gen_speed(), gen_color())
        balls.append(i)
    return balls


def update_canvas():
    for ball in balls_list:
        ball.move()
    window.after(10, update_canvas)


if __name__ == '__main__':
    window = Tk()
    window.title("Balls generate_balls")
    canvas = Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()
    balls_list = generate_balls()
    update_canvas()
    window.mainloop()
