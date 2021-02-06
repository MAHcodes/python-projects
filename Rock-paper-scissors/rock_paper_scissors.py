import random
counter = 0
play = True
obj = {"P": "Paper", "S": "Scissors", "R": "Rock"}
computer_wins = 0
user_wins = 0
line = "-" * 25

print("Welcome to Rock, Paper and Scissors Game")

while play:
    rounds = int(input("How many rounds you like to play?: "))
    while counter < rounds:
        user_choice = input(f"\nRound: {counter + 1}\nScore: You {user_wins} | Computer {computer_wins}\n{line}\nChoose (R) for Rock, (P) for Paper and (S) for Scissors: ").upper()
        computer_choice = random.choice(["R", "P", "S"])
        if (user_choice != "R") and (user_choice != "S") and (user_choice != "P"):
            print("Invalid Input, Please try again!")
            continue
        else:
            if user_choice == computer_choice:
                print(f"You And The Computer Chose: {obj[computer_choice]}\nIts a tie!")
                counter += 1
            if (user_choice[0] == "R" and computer_choice == "S") or (user_choice[0] == "S" and computer_choice == "P") or (user_choice[0] == "P" and computer_choice == "R"):
                print(f"You Chose {obj[user_choice]}\nComputer Chose {obj[computer_choice]}\nYou Win Round {counter + 1}")
                counter += 1
                user_wins += 1
            if (user_choice[0] == "R" and computer_choice == "P") or (user_choice[0] == "S" and computer_choice == "R") or (user_choice[0] == "P" and computer_choice == "S"):
                print(f"You Chose {obj[user_choice]}\nThe Computer Chose {obj[computer_choice]}\nComputer Win Round {counter + 1}")
                counter += 1
                computer_wins += 1

    if computer_wins == user_wins :
        print(f"\n{line}\nDraw! Your and the Computers scores {computer_wins} wins!\n{line}")
    elif user_wins > computer_wins:
        print(f"\n{line}\nCONGRATULATIONS! You Win!...\n{line}")
    else:
        print(f"\n{line}\nUnfortunately! The computer wins...\n{line}")
    play = input("Enjoy the game? Press any key to play again or 'E' for exit: ").upper()
    if play[0] == "E":
        play = False
    else:
        counter = 0
        user_wins = 0
        computer_wins = 0