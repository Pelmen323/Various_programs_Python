import random
from tkinter import *

num_of_rounds = 0
current_round = 0
possible_choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

# Everything that should not be available is blocked. Background colors are changed depending on win/lose/draw
def start_a_game():
    global num_of_rounds
    start.config(state=DISABLED)
    num_of_rounds = scale.get()
    rock.config(state=NORMAL)
    paper.config(state=NORMAL)
    scissors.config(state=NORMAL)
    info_label.config(text='')
    results_label.config(text='Rock, Paper or Scissors?')
    window.config(background='#F0F0F0')
    scale.config(background='#F0F0F0')
    rounds_label.config(background='#F0F0F0')
    scale.config(background='#F0F0F0')
    info_label.config(background='#F0F0F0')
    results_label.config(background='#F0F0F0')


def select(argument):
    global num_of_rounds
    global current_round
    global possible_choices
    global player_score
    global computer_score
    # Generate PC choice and get players choice
    computer_choice = random.choice(possible_choices)
    player_choice = argument
    current_round += 1
    # Lets see if player or PC won:

    if player_choice == computer_choice:
        info_label.config(text="Computer: "+ computer_choice + ", Player: "+ player_choice + ". Draw!")

    elif player_choice == 'rock':                                                                               # Rock
        if computer_choice == 'paper':
            info_label.config(text="Computer: "+ computer_choice + ", Player: "+ player_choice + ". Defeat!")
            computer_score += 1
        if computer_choice == 'scissors':
            info_label.config(text="Computer: "+ computer_choice + ", Player: "+ player_choice + ". Win!")
            player_score += 1
    elif player_choice == 'paper':                                                                              # Paper
        if computer_choice == 'scissors':
            info_label.config(text="Computer: "+ computer_choice + ", Player: "+ player_choice + ". Defeat!")
            computer_score += 1
        if computer_choice == 'rock':
            info_label.config(text="Computer: "+ computer_choice + ", Player: "+ player_choice + ". Win!")
            player_score += 1
    elif player_choice == 'scissors':                                                                           # Scissors
        if computer_choice == 'rock':
            info_label.config(text="Computer: "+ computer_choice + ", Player: "+ player_choice + ". Defeat!")
            computer_score += 1
        if computer_choice == 'paper':
            info_label.config(text="Computer: "+ computer_choice + ", Player: "+ player_choice + ". Win!")
            player_score += 1

    # Visually display hom many rounds left
    scale.set(scale.get()-1)
    # check if num of rounds does not exceed
    if current_round == num_of_rounds:
        # Print the game result and change the theme
        if player_score > computer_score: 
            results_label.config(text="Player wins! The score is {} vs {}.".format(player_score, computer_score))
            window.config(background='#bbff99')
            scale.config(background='#bbff99')
            rounds_label.config(background='#bbff99')
            scale.config(background='#bbff99')
            info_label.config(background='#bbff99')
            results_label.config(background='#bbff99')
        if player_score < computer_score: 
            results_label.config(text="Computer wins! The score is {} vs {}.".format(player_score, computer_score))
            window.config(background='#ff9999')
            scale.config(background='#ff9999')
            rounds_label.config(background='#ff9999')
            scale.config(background='#ff9999')
            info_label.config(background='#ff9999')
            results_label.config(background='#ff9999')
        if player_score == computer_score: 
            results_label.config(text="Draw! The score is {} vs {}.".format(player_score, computer_score))
            window.config(background='#fffa99')
            scale.config(background='#fffa99')
            rounds_label.config(background='#fffa99')
            scale.config(background='#fffa99')
            info_label.config(background='#fffa99')
            results_label.config(background='#fffa99')
        # Clear everything

        current_round = 0
        player_score = 0
        computer_score = 0
        start.config(state=NORMAL)
        rock.config(state=DISABLED)
        paper.config(state=DISABLED)
        scissors.config(state=DISABLED)


window = Tk()
window.title('Rock, Paper, Scissors')
window.geometry('400x300')

rock_img = PhotoImage(file='Images\\rock.png') 
paper_img = PhotoImage(file='Images\\paper.png') 
scissors_img = PhotoImage(file='Images\\scissors.png') 

rounds_label = Label(window, text='Select number of rounds:')
scale = Scale(window, from_=1, to=10, orient=HORIZONTAL, length=300)
start = Button(window, text='Start a game!', command=start_a_game)
info_label = Label(window)
results_label = Label(window)

frame = Frame(window, width=15)
rock = Button(frame, text='Rock', image=rock_img, compound=BOTTOM, command=lambda: select('rock'), state=DISABLED)
paper = Button(frame, text='Paper', image=paper_img, compound=BOTTOM, command=lambda: select('paper'), state=DISABLED)
scissors = Button(frame, text='Scissors', image=scissors_img, compound=BOTTOM, command=lambda: select('scissors'), state=DISABLED)

rounds_label.pack()
scale.pack()
start.pack()
info_label.pack()
results_label.pack()
frame.pack()

rock.pack(side=LEFT)
paper.pack(side=LEFT)
scissors.pack(side=LEFT)

window.mainloop()
