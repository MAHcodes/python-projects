while True:
    operation = int(input("1. Add\n2. Subtract\n3. Multiplty\n4. Devide\n5. Exit\n>>> "))
    if operation == 5:
        break
    if operation == 1 or operation == 2 or operation == 3 or operation == 4:
        first_num = int(input("Enter first number: "))
        second_num = int(input("Enter second number: "))
    else:
        print("Enter number of your choice from 1 to 5\n")

    if operation == 1:
        print(f"\nAddition = {first_num + second_num}\n")
    elif operation == 2:
        print(f"\nSubtraction = {first_num - second_num}\n")
    elif operation == 3:
        print(f"\nMultiplication = {first_num * second_num}\n")
    elif operation == 4:
        print(f"\nDevision = {first_num / second_num}\n")


