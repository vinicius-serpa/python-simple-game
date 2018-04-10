import random


def play():
    print("*********************************")
    print("*********Divination Game!********")
    print("*********************************")

    print("select level: (1) easy, (2) normal, (3) hard")

    level = int(input("Type level:"))

    if (level == 1):
        total_tentative = 20
    elif (level == 2):
        total_tentative = 10
    else:
        total_tentative = 5

    secret_number = random.randrange(1, 101)  # random use milliseconds by default to determine the seed
    points = 1000

    for tentative in range(1, total_tentative + 1):

        print("{} of {} - ".format(tentative, total_tentative), end=" ")

        user_number_str = input("Type your number between 1 and 100: ")
        user_number = int(user_number_str)

        if (user_number < 1 or user_number > 100):
            print("Type number between 1 and 100")
            continue

        win = user_number == secret_number
        major = user_number > secret_number
        minor = user_number < secret_number

        print("Your number is: {}.".format(user_number_str), end=" ")

        if win:
            print("You win!")
            print("Total points: {}".format(points))
            break
        else:
            print("Wrong!", end=" ")
            points = points - abs(user_number - secret_number)
            if (tentative != total_tentative):
                if major:
                    print("Try a minor number.")
                elif minor:
                    print("Try a major number.")

    print("The correct number is {}".format(secret_number))
    print("Game over")


if (__name__ == "__main__"):
    play()
