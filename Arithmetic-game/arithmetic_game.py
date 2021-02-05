import random
play = True
counter = 0
operations = ["+", "-", "*", "/"]
op = ''
print("             Welcome to Math quiz")


def main():
    global op
    while True:
        diff = int(input("1. Easy\n2. Normal\n3. Hard\n4. Extreme\nChoose the difficulty level you want to play: "))
        if diff == 1:
            op = operations[0]
            break
        elif diff == 2:
            op = operations[0:2]
            break
        elif diff == 3:
            op = operations[0:3]
            break
        elif diff == 4:
            op = operations
            break
        else:
            print("Invalid input, please try again")
            continue
    start(3)


def start(lives):
    global counter
    global op
    for i in range(lives):
        while lives > i:
            opp = random.choice(op)
            if opp == "+":
                first_num = random.randint(2, 50)
                second_num = random.randint(2, 50)
                while True:
                    answer = int(input(f"\n{first_num} + {second_num} = "))
                    if answer != first_num + second_num:
                        if lives > 1:
                            print(f"Wrong! try again... You have {lives - 1} lives left")
                            lives -= 1
                            continue
                        else:
                            print(f"Wrong! You have {lives - 1} left")
                            lives -= 1
                            break
                    elif answer == first_num + second_num:
                        (print("Correct!"))
                        counter += 1
                        first_num = random.randint(1, 50)
                        second_num = random.randint(1, 50)
                        break
            elif opp == "-":
                first_num = random.randint(25, 50)
                second_num = random.randint(2, 24)
                while True:
                    answer = int(input(f"\n{first_num} - {second_num} = "))
                    if answer != first_num - second_num:
                        if lives > 1:
                            print(f"Wrong! try again... You have {lives - 1} lives left")
                            lives -= 1
                            continue
                        else:
                            print(f"Wrong! You have {lives - 1} left")
                            lives -= 1
                            break
                    elif answer == first_num - second_num:
                        (print("Correct!"))
                        counter += 1
                        first_num = random.randint(25, 50)
                        second_num = random.randint(1, 24)
                        break
            elif opp == "*":
                first_num = random.randint(2, 10)
                second_num = random.randint(5, 10)
                while lives > i:
                    answer = int(input(f"\n{first_num} * {second_num} = "))
                    if answer != first_num * second_num:
                        if lives > 1:
                            print(f"Wrong! try again... You have {lives - 1} lives left")
                            lives -= 1
                            continue
                        else:
                            print(f"Wrong! You have {lives - 1} left")
                            lives -= 1
                            break
                    elif answer == first_num * second_num:
                        (print("Correct!"))
                        counter += 1
                        first_num = random.randint(1, 10)
                        second_num = random.randint(5, 10)
                        break
            elif opp == "/":
                first_num = random.randint(10, 50)
                second_num = random.randint(2, 10)
                while lives > i:
                    answer = int(input(f"\n{first_num} // {second_num} = "))
                    if answer != first_num // second_num:
                        if lives > 1:
                            print(f"Wrong! try again... You have {lives - 1} lives left")
                            lives -= 1
                            continue
                        else:
                            print(f"Wrong! You have {lives - 1} lives left")
                            lives -= 1
                            break
                    elif answer == first_num // second_num:
                        (print("Correct!"))
                        counter += 1
                        first_num = random.randint(10, 50)
                        second_num = random.randint(2, 10)
                        break
    print(f"You got {counter} correct answers!")
    again = input("Enjoy the game? press any key to play again or (E) to exit: ").upper()
    if again[0] == "E":
        pass
    else:
        main()


if __name__ == '__main__':
    main()