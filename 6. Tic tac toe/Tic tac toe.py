from tkinter import *
import random

# Add the text to the button, trigger the check_winner func, print status
def next_turn(x, y):
    global player
    if buttons[x][y]['text'] == "": 
        buttons[x][y]['text'] = player
        if check_winner() == False:
            if player == players[0]: player = players[1]
            elif player == players[1]: player = players[0]
            label.config(text=player + ' turn')
        elif check_winner() == True:
            label.config(text=player + ' wins!')
        elif check_winner() == 'Tie':
            label.config(text='Tie!')

# Check all possible win conditions and tie possibility
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '': 
            buttons[row][0].config(bg='Green') 
            buttons[row][1].config(bg='Green')
            buttons[row][2].config(bg='Green')
            return True
    for column in range(3):    
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '': 
            buttons[0][column].config(bg='Green') 
            buttons[1][column].config(bg='Green')
            buttons[2][column].config(bg='Green')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '': 
            buttons[0][0].config(bg='Green') 
            buttons[1][1].config(bg='Green')
            buttons[2][2].config(bg='Green')
            return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '': 
            buttons[0][2].config(bg='Green') 
            buttons[1][1].config(bg='Green')
            buttons[2][0].config(bg='Green')
            return True
    doesnt_have_empty_spaces = True
    for row in range(3):
        if doesnt_have_empty_spaces == False: break
        for column in range(3):
            if buttons[row][column]['text'] == '': 
                doesnt_have_empty_spaces = False
                break

    if doesnt_have_empty_spaces == True: return 'Tie'
    else: return False

# Clear the board
def new_game():
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg='#F0F0F0')
    label.config(text='New game begins!')

window = Tk()
window.title('Tic tac toe')
window.geometry('500x500')
window.config(bg='#faf598')

players = ['X', 'O']
player = random.choice(players)
buttons =  [[0,0,0],
            [0,0,0],
            [0,0,0]]

label = Label(window, text= player + ' turn', font=('Consolas', 30), bg='#faf598')
label.pack()

frame = Frame(window)
frame.pack()

# Replace the contents of buttons list of lists with buttons objects
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', width=10, height=4,\
                                        command=lambda x=row, y=column :next_turn(x, y))
                                        # ^This is has to be written, otherwise the args are not passed
        buttons[row][column].grid(row=row, column=column)

newgame_btn = Button(window, text='Start a new game', font=('Consolas', 15), command=new_game)
newgame_btn.pack()
window.mainloop()