from tkinter import *
from tkinter import colorchooser
import random
from idlelib.tooltip import Hovertip
                                    # Constants
GAME_WIDTH = 700                    # Canvas width
GAME_HEIGHT = 700                   # Canvas height
BODY_PARTS = 3                      # Starting blocks of a snake
FONT_SETTINGS = ('Consolas', 20)    # Label font settings

                                    # Variables - some vars are declared later
speed = 100                         # Default speed - update once each 100ms
snake_color = '#00FF00'             # Default snake color
food_color = '#db5153'              # Default food color
background_color = '#000000'        # Default bg color
FONT_SETTINGS = ('Consolas', 20)    # Label font settings


###########################
# Snake object
###########################
class Snake():

    def __init__(self):
        self.length = BODY_PARTS
        self.coordinates = []               # Needed to draw a new square
        self.squares = []                   # Needed to delete square objects 

        for i in range(BODY_PARTS):         # Create a staring list of lists with snake blocks coordinates
            self.coordinates.append([0,0])
    
        for x, y in self.coordinates:       # For each item in the list - draw a square and add this object to a list of squares
            square = canvas.create_rectangle(x, y, x+space_size.get(), y+space_size.get(), fill=snake_color, tag='snake')
            self.squares.append(square)


class Food():
    def __init__(self):                     # This should be exclusive (food should spawn in the field), so -1,. Sadly this sometimes will spawn the food above the snake
        x_coords = random.randint(0, int(GAME_WIDTH/space_size.get())-1) * space_size.get()
        y_coords = random.randint(0, int(GAME_HEIGHT/space_size.get())-1) * space_size.get()
        self.coordinates = [x_coords, y_coords]   # Create a new food object                                                              # To make deletion easier
        canvas.create_rectangle(x_coords, y_coords, x_coords+space_size.get(), y_coords+space_size.get(), fill=food_color, tag='food')

###########################
# Main function
###########################

def next_turn(snake, food):
    global direction
    global new_direction
    # Change the direction of the snake
    if new_direction.get() == 'up' and direction != 'down': direction = 'up'
    if new_direction.get() == 'down' and direction != 'up': direction = 'down'
    if new_direction.get() == 'left' and direction != 'right': direction = 'left'
    if new_direction.get() == 'right' and direction != 'left': direction = 'right' 
    # Snake head coordinates from the list and calculate the next change 
    x, y = snake.coordinates[0] 
    if direction == 'up':
        y -= space_size.get()
    elif direction == 'down':
        y += space_size.get()
    elif direction == 'left':
        x -= space_size.get()
    elif direction == 'right':
        x += space_size.get()

    # Update coordinates of the snake head in the list
    snake.coordinates.insert(0, (x,y))
    # Create a new head rectangle
    global snake_color
    square = canvas.create_rectangle(x, y, x+space_size.get(), y+space_size.get(), fill=snake_color)
    # Update the snake's list of rectangles
    snake.squares.insert(0, square)

    # Eat that food - if head of the snake coords matches the food coords, the snake tail will not be cut. Also, increases the snake speed
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        global speed
        score += 1
        if speed > 60: speed -= 1
        score_label.config(text='Score: {}'.format(score))

        canvas.delete('food')
        food = Food()

    # The tail of the snake is deleted each turn when food is not eaten
    else: 
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1] 

    # If the collision is triggered - end the game, else start again
    if check_collisions(snake) == False: game_over()
    else: window.after(speed, next_turn, snake, food)

###########################
# Secondary functions
###########################


def check_collisions(snake):
    # Unpack the head of the snake coords
    x, y = snake.coordinates[0]

    if x < 0 or y < 0 or x >= GAME_WIDTH or y >= GAME_HEIGHT:
        return False
    # Check if anything in the snake coords that is not head of the snake matches the head coords:
    for body_part in snake.coordinates[1:]:
        if body_part == (x,y):
            return False


def game_over():                        # Unlock the restart button and the space size config
    global score
    score_label.config(text='Game over! Your score: {}'.format(score))
    start_button.config(state=NORMAL)
    space_size_chooser.config(state=NORMAL)
    snake_color_button.config(state=NORMAL)
    food_color_button.config(state=NORMAL)
    background_color_button.config(state=NORMAL)


def start_the_game():                   # Reset everything, block the core settings and the start button
    global score
    global direction
    global speed
    canvas.delete('all')                # Purge it all
    score = 0
    direction = 'down' 
    new_direction.set('down')           # To avoid the bug, when the snake is dead on start due to the immediate collision
    speed = 100                         # The speed is back to normal
    snake = Snake()                     # Generate a new snake
    food = Food()
    start_button.config(state=DISABLED)
    space_size_chooser.config(state=DISABLED)
    snake_color_button.config(state=DISABLED)
    food_color_button.config(state=DISABLED)
    background_color_button.config(state=DISABLED)
    score_label.config(text='Score: {}'.format(score))
    next_turn(snake, food)

###########################
# Customization
###########################

def change_snake_color():
    global snake_color
    x = colorchooser.askcolor(title='Pick snake color')[1]
    snake_color = x
    snake_color_button.config(bg=x)

def change_food_color():
    global food_color
    x = colorchooser.askcolor(title='Pick food color')[1]
    food_color = x
    food_color_button.config(bg=x)

def change_background_color():
    global background_color
    canvas.config(bg=colorchooser.askcolor(title='Pick background color')[1])

def change_space_size():
    global space_size
    space_size.set(space_size_chooser.get())

###########################
# Window
###########################
window = Tk()
window.title('Snake game')
window.resizable(False, False)                  #Expansion of the window is blocked for each direction

space_size = IntVar(window)                     #Define window variables and set base values
space_size.set(35)
new_direction = StringVar(window)
new_direction.set('down')


###########################
# Settings frame
###########################
frame = Frame(window)

snake_color_button = Button(frame, text='Snake color', width=15, command=change_snake_color, bg=snake_color)
snake_color_button.pack(side=LEFT)
tip_snake_clr = Hovertip(snake_color_button,'Change a snake color', hover_delay=500)

food_color_button = Button(frame, text='Food color', width=15, command=change_food_color, bg=food_color)
food_color_button.pack(side=LEFT)
tip_food_clr = Hovertip(food_color_button,'Change food color', hover_delay=500)

background_color_button = Button(frame, text='Background color', width=15, command=change_background_color)
background_color_button.pack(side=LEFT)
tip_bkg_clr = Hovertip(background_color_button,'Change background color', hover_delay=500)

space_size_chooser = OptionMenu(frame, space_size,*[10, 25, 35, 50, 70])
space_size_chooser.pack(side=LEFT)
tip_sschooser = Hovertip(space_size_chooser,'Change the space size. The lower the value - \nthe smaller the objects (snake/food)', hover_delay=500)

help_button = Button(frame, text='Help', width=15)
help_button.pack(side=RIGHT)
tip_help = Hovertip(help_button,"Hi! This is a snake game. The rules are simple:\n\nControls:\nW, A, S, D \\ arrows - change the snake direction\n\nRules:\nWhen snake eats a food item, its size and speed increases\nIf the snake collides with the borders or with its own body - the game will be over\n\nThe scale of the game can be increased/decreased by changing the dropdown number value:\n10 - a lot of free space,\n35 - default value, \n70 - free space is severely limited\n\n A tip - You can change the snake direction once per movement tick. You can't change the direction to the opposite in one tick.\n The bigger the snake - the faster it move (up to 80 percent faster) and the faster its direction can be changed", hover_delay=500)

frame.pack()

###########################
# Start the game, info label, canvas and placement of a window
###########################

start_button = Button(window, text='Start the game', command=start_the_game)
start_button.pack()
tip_bkg_clr = Hovertip(start_button,'What are you waiting for? :)', hover_delay=1000)
score_label = Label(window, font=FONT_SETTINGS, text='Start the game or customize the settings!')
score_label.pack()

canvas = Canvas(window, bg=background_color, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

    # Place the window to the center of the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
    # Set a new coords for window - get top left corner
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


    # Key bindings to change the directions - they don't call a function, instead they change the variable that is checked each tick. 
    # Earlier it was possible to suicide by changing the direction too fast, this is why the change of direction is tied to the main function and not in a separate one
window.bind("<w>", lambda x:new_direction.set('up')) 
window.bind("<a>", lambda x:new_direction.set('left'))
window.bind("<s>", lambda x:new_direction.set('down'))  
window.bind("<d>", lambda x:new_direction.set('right'))
window.bind("<Up>", lambda x:new_direction.set('up')) 
window.bind("<Left>", lambda x:new_direction.set('left'))   
window.bind("<Down>", lambda x:new_direction.set('down'))
window.bind("<Right>", lambda x:new_direction.set('right'))



window.mainloop()