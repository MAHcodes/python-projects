import random
rounds_count = 0
player1_win = 0
player2_win = 0
line = "-"*20


while True:
    print(" WELCOME TO DICE ROLLING GAME! ")
    player1_name = input("Enter 1st player name: ").title()
    player2_name = input("Enter 2nd player name: ").title()
    print(f"{line}\n{player1_name} -> 1st Player\n{player2_name} -> 2nd Player\n{line}")
    rounds = int(input("Enter how many rounds you want to play? "))

    def roll_dice():
        global rounds_count
        global player1_win
        global player2_win
        global rounds
        while rounds_count < rounds:
            print(f'\n{line}\nRound : {rounds_count+1}\n{line}')
            input(f'{player1_name} enter "r" to roll the dice: ')
            player1 = random.randint(1, 6)
            print(f'{player1_name} Roll: {player1}\n')
            input(f'{player2_name} enter "r" to roll the dice: ')
            player2 = random.randint(1, 6)
            print(f'{player2_name} Roll: {player2}')
            rounds_count += 1
            if player1 == player2:
                print(f'\nRound: {rounds_count} Draw!')
            elif player1 > player2:
                print(f'\n{player1_name} Wins The {rounds_count} Round!')
                player1_win += 1
            else:
                print(f'\n{player2_name} Wins The {rounds_count} Round!')
                player2_win += 1
        if player1_win == player2_win:
            print("\nDraw! You both wins " + str(player1_win) + " Rounds!\n")
            again = input("Do You Want To Play Again? (Y/n): ").upper()
        elif player1_win > player2_win:
            print(f"\n{line}\n{player1_name} Wins!\n{line}")
            again = input("Do You Want To Play Again? (Y/n): ").upper()
        else:
            print(f"\n{line}\n{player2_name} Wins!\n{line}")
            again = input("Do You Want To Play Again? (Y/n): ").upper()

        if again == "Y":
            rounds_count = 0
            rounds = int(input("\nEnter how many rounds you want to play? "))
            roll_dice()
        elif again == "N":
            print("EXITING... HOPE YOU ENJOY THE GAME ;)")
    break

if __name__ == "__main__":
    roll_dice()
