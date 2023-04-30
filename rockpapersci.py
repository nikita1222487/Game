import random

print("Let's play Rock-Paper-Scissors!")
print("The first to win three rounds wins the game.")


choices = ["rock", "paper", "scissors"]

# initialize scores
player_score = 0
computer_score = 0

# loop until one player wins three rounds
while player_score < 3 and computer_score < 3:

    # get player's choice
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    # get computer's choice
    computer_choice = random.choice(choices)

    # determine winner of this round
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        player_score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
        player_score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # print current scores
    print("Player: ", player_score)
    print("Computer: ", computer_score)

# print final result
if player_score > computer_score:
    print("Congratulations! You win the game!")
else:
    print("Sorry, you lost the game.")
