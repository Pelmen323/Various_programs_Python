from tkinter import *
import time
import random

WIDTH = 1000
HEIGHT = 1000

window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT)
canvas.pack()

class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, x+diameter, y+diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.diameter = diameter

    def move(self):
        coords = self.canvas.coords(self.image)
        if coords[2] >= self.canvas.winfo_width() or coords[0] <= 0:
            self.xVelocity = -self.xVelocity
        if coords[3] >= self.canvas.winfo_height() or coords[1] <= 0:
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)

def gen_speed(): return random.randint(0,10)
def gen_size(): return random.randint(10,299)
def gen_coords(): return random.randint(300,699)
def gen_color(): return ('#%06X' % random.randint(0, 0xFFFFFF))

def generator():
    number = 'x'
    balls = []
    while number.isdigit() == False: number = input('How many balls do you want?: ')
    for i in range(int(number)):
        i = Ball(canvas, gen_coords(), gen_coords(), gen_size(), gen_speed(), gen_speed(), gen_color())
        balls.append(i)
    return balls
    
balls_list = generator()

while True:   
    for i in balls_list:
        i.move()  
    window.update()
    time.sleep(0.01)

window.mainloop()