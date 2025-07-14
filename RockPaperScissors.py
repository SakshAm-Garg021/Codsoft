import random
def user_choice():
    while True:
        Player_choice=input("\nChoose any one of them (rock, paper or scissors): ").lower()
        if Player_choice in ["rock","paper","scissors"]:
            return Player_choice
        else :
            print("Invalid Input!\n Please Enter (rock, paper or scissors) ")
def Computer_choice():        
    choice=("rock","paper","scissors")
    computer_cho= ''.join(random.choice(choice))
    return computer_cho
def game(Player_choice,computer_cho):
    if Player_choice==computer_cho:
        return "tie"
    elif (Player_choice=='rock' and computer_cho=='scissors') or (Player_choice=='scissors'and computer_cho=='paper')or(Player_choice=='paper' and computer_cho=='rock'):
        return "Player"
    else:
        return "Computer"
player_score=0
computer_score=0
print("Welcome in Game World!")
while True:
    Player_choices=user_choice()
    computer_choices=Computer_choice()
    winner=game(Player_choices,computer_choices)
    print("Player choice =",Player_choices,"\nComputer choice =",computer_choices,"\nWinner =",winner)
    if winner=="tie":
        player_score += 0
        computer_score += 0
    elif winner=="Player":
        player_score+=1

    elif winner=="Computer":
        computer_score+=1
    print("Player Score =",player_score,"\tComputer Score =",computer_score)
    player_again=input("Do you want to play again(YES/NO): ").lower()
    if player_again=="no":
        print("Good Bye!")
        break
