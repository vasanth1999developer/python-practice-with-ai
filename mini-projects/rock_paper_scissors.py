import random


def get_choices():
    player_choice = input("Enter a choice ( rock, paper, scissors: =")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    random_choices = {"player": player_choice, "computer": computer_choice}
    return random_choices


print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def check_win(player, computer):

    print(f"you chose {player} , computer chose {computer}")

    if player == computer:
        return "tie!"
    elif player == "rock" :
        if computer == "scissors":
          return "rock smashes scissor! you wins"
        else:
            return "paper cover rock!!! you lose"
    elif player == "paper" :
        if computer == "rock":
          return "paper cover rock! you wins"
        else:
            return "scissors cut paper!!! you lose"
    elif player == "scissors" :
        if computer == "paper":
          return "scissors cut paper! you wins"
        else:
          return "rock smashes scissors!!! you lose"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)