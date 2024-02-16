import random

print("This is the rock paper scissors game made using Python.")
cpuchoice = ['r', 'p', 's']
user1_score = 0
user2_score = 0

def play(user1, user2=None):
    global user1_score, user2_score
    
    while True:
        if user2 is None:
            user2 = random.choice(cpuchoice)
        
        if user1 not in cpuchoice or user2 not in cpuchoice:
            print("Invalid choices")
            continue
        elif user1 == user2:
            print("It's a tie!")
        elif (user1 == 'r' and user2 == 's') or (user1 == 's' and user2 == 'p') or (user1 == 'p' and user2 == 'r'):
            print("Player 1 wins")
            user1_score += 1
        else:
            print("Player 2 wins")
            user2_score += 1

        print("Scores: Player 1 -", user1_score, ", Player 2 -", user2_score)
        break

def inputuser():
    while True:
        players = int(input("Enter the number of players: "))
        if players > 2:
            print("Maximum 2 players allowed.")
            continue
        elif players == 1:
            user1 = input("Player 1: ROCK, PAPER, SCISSORS, SHOOT!")
            play(user1)
        elif players == 2:
            user1 = input("Player 1: ROCK, PAPER, SCISSORS, SHOOT!")
            user2 = input("Player 2: ROCK, PAPER, SCISSORS, SHOOT!")
            play(user1, user2)
        else:
            print("Invalid number of players.")
            continue

        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() != "yes":
            print("Thanks for playing!")
            break

inputuser()
