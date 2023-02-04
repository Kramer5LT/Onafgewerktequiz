import random

numWins = 0
numWinsComputer = 0

options = ["rock", "paper", "scissors"]

while True:
    choice = input("Type rock, paper, scissors or q to quit: ")
    choice = choice.lower()
    if choice == "q":
        break

    if choice not in options:
        print("Please select a valid option\n")
        continue

    computer_choice = random.choice(options)

    if choice == computer_choice:
        print("It's a tie")
    elif choice == "rock" and computer_choice == "scissors":
        print("You won")
        numWins += 1
    elif choice == "paper" and computer_choice == "rock":
        print("You won")
        numWins += 1
    elif choice == "scissors" and computer_choice == "paper":
        print("You won")
        numWins += 1
    else:
        print("You lost")
        numWinsComputer += 1

    print("Your wins: ", numWins)
    print("Computer wins: ", numWinsComputer)