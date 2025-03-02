- Project name: Rock-Paper-Scissors game
- Discription: In this project we will generate a random number set (0, 1, 2) to represent (rock, paper, scissors) for the game. 
             Create a while loop that simulates a game where the user competes against the computer. The user wins if their input matches one of the predefined winning options; otherwise, the computer wins.

                        
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit the game.  ").lower()
    if user_input == "q":
        break #or quit()

    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!!")
        user_wins += 1
    
    else:
        print("You lost!!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times")

print("See you next time!!")

