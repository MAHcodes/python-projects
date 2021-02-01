import random

play = True


def guess(x):
    global play
    random_number = random.randint(1, x)
    guess = 0
    counter = 1
    while guess != random_number:
        guess = int(input(f'Guess a number from 1 to {x}: '))
        if guess > random_number:
            print("Try Again, Too High")
            counter += 1
        elif guess < random_number:
            print("Try Again, To Low")
            counter += 1
    print(f"Congrats you guess the number {random_number} correctly!!, You Tried {counter} times")
    random_number = random.randint(1, x)
    guess = 0
    play = input("Enjoy the game? Press any key to play again or 'E' for exit: ")
    if play[0].upper() == 'E':
        play = False


def pc_guess(x):
    global play
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        pc = random.randint(low, high)
        feedback = input(f"Is ({pc}) Too high(h), Too minimum_num or Correct(c)? ").lower()
        if feedback == "h":
            high = pc - 1
        elif feedback == "l":
            low = pc + 1
    print(f"Yay! the computer guessed your number {pc} correctly!")
    play = input("Enjoy the game? Press any key to play again or 'E' for exit: ")
    feedback = ''
    if play[0].upper() == 'E':
        play = False


while play:
    while True:
        choice = int(
            input("\n1. Guess a random number\n2. The computer guess your number\nWhat do you like to play?: "))
        if choice == 1 or choice == 2:
            break
        else:
            print("Please choose a valid number!")
            continue
    x = int(input("Enter a maximum number to guess: "))
    if choice == 1:
        guess(x)
    elif choice == 2:
        pc_guess(x)
