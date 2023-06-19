import random

choices = ['rock', 'paper', 'scissors']

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

def print_choices():
    print("Available choices: ")
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

def print_score(player_score, computer_score):
    print(f"Score - Player: {player_score}  Computer: {computer_score}")

def play_game():
    player_score = 0
    computer_score = 0
    total_rounds = 0

    print("Welcome to Rock Paper Scissors!")
    name = input("Enter your name: ")

    while True:
        print_choices()
        player_choice = input("Enter your choice (1-3): ")
        if player_choice.isdigit() and 1 <= int(player_choice) <= 3:
            player_choice = choices[int(player_choice) - 1]
        else:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"{name}'s choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)

        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'player':
            print(f"{name} wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        total_rounds += 1
        print_score(player_score, computer_score)

        if total_rounds >= 5:
            if player_score > computer_score:
                print(f"{name} is the winner!")
            elif player_score < computer_score:
                print("Computer is the winner!")
            else:
                print("It's a tie overall!")

            play_again = input("Play again? (y/n): ")
            if play_again.lower() == 'y':
                player_score = 0
                computer_score = 0
                total_rounds = 0
                continue
            else:
                break

play_game()
