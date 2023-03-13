import random

print("Welcome to Rock, Paper, Scissors!")

options = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Choose rock, paper, or scissors: ")
    
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    

    ai_choice = random.choice(options)
    print("Ai chooses", ai_choice)
    
    if player_choice == ai_choice:
        print("Tie!")
    elif player_choice == "rock" and ai_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and ai_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and ai_choice == "paper":
        print("You win!")
    else:
        print("Ai wins!")
    
    play_again = input("Play again? (y/n) ")
    if play_again.lower() != "y":
        break

print("Thanks for playing my game!")
