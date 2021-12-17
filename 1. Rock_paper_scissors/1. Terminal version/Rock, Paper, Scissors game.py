import random


def results(player_score, pc_score):
    if player_score > pc_score:
        return f"Player wins! The score is {player_score} vs {pc_score}."
    elif player_score < pc_score:
        return f"Computer wins! The score is {player_score} vs {pc_score}."
    elif player_score == pc_score:
        return f"Tie! The score is {player_score} vs {pc_score}."


print("Hello! This is a small 'Rock, paper, tie' game, made as a Python practice. The input is not case-sensitive. Have fun!\n")
while True:
    choices, num_of_rounds, player_score, computer_score = ['rock', 'paper', 'scissors'], 'a', 0, 0     
    while num_of_rounds.isdigit() is False:
        num_of_rounds = input("How many rounds do you want to play?: ")
    for i in range(int(num_of_rounds)):
        player_choice = None
        computer_choice = random.choice(choices)

        while player_choice not in choices:
            player_choice = input("Rock, paper or scissors?: ").lower()

        if player_choice == computer_choice:
            print("\nComputer: ", computer_choice)
            print("Player: ", player_choice)
            print("Tie!")

        elif player_choice == 'rock':
            if computer_choice == 'paper':
                print("\nComputer: ", computer_choice)
                print("Player: ", player_choice)
                print("Lose!")
                computer_score += 1
            if computer_choice == 'scissors':
                print("\nComputer: ", computer_choice)
                print("Player: ", player_choice)
                print("Win!")
                player_score += 1
        elif player_choice == 'paper':
            if computer_choice == 'scissors':
                print("\nComputer: ", computer_choice)
                print("Player: ", player_choice)
                print("Lose!")
                computer_score += 1
            if computer_choice == 'rock':
                print("\nComputer: ", computer_choice)
                print("Player: ", player_choice)
                print("Win!")
                player_score += 1
        elif player_choice == 'scissors':
            if computer_choice == 'rock':
                print("\nComputer: ", computer_choice)
                print("Player: ", player_choice)
                print("Lose!")
                computer_score += 1
            if computer_choice == 'paper':
                print("\nComputer: ", computer_choice)
                print("Player: ", player_choice)
                print("Win!")
                player_score += 1

    print(results(player_score, computer_score))
    play_again = input("Play again? (yes/y to continue): ").lower()
    if play_again == 'yes' or play_again == 'y':
        player_score, computer_score = 0, 0       # Restarting - resetting the scores
    else:
        break
print("Bye!")
