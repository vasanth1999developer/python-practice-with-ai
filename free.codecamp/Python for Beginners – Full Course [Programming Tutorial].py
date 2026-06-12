import random


def get_choices():
    player_choice = input("Enter a choice ( rock, paper, scissor: ")
    options = ["rock", "paper", "sccisor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


choices = get_choices()

print(choices)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def check_win(player, computer):
    print(f"you chose {player} , computer chose {computer}")
    if player == computer:
        return "tie!"
    elif player == "rock" and computer == "scissors":
        return "rock smashes scissor! you wins"
    elif player == "rock" and computer == "paper":
        return "paper cover rock!!! you lose"


check_win("rock", "scissor")




age = 20

if age >= 18:
    print("you are adult")
elif age < 12:
    print("you are a teenager")
elif age < 1:
    print("you are a child")
else:
    print("you are a baby")

# age = 25
# print(f"jin is {age} years old")

