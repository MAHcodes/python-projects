import csv

with open("users.csv", "r+") as users:
    csv_reader = csv.reader(users)
    next(csv_reader)
    for user in csv_reader:
        username = input("Enter username: ")
        while username not in user[0]:
            username = input("Username not found, Try again: ")
        passwd = input("Enter Password: ")
        while passwd not in user[1]:
            passwd = input("Wrong password, Try again: ")
        print("You Have Successfully logged in")