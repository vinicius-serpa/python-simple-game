print("*********************************")
print("*********Divination Game!********")
print("*********************************")

secret_number = 42
tentative = 1
total_tentative = 3

while (tentative <= total_tentative):

    print("Tentative {} of {}".format(tentative, total_tentative))

    user_number_str = input("Type your number: ")
    user_number = int(user_number_str)

    win = user_number == secret_number
    major = user_number > secret_number
    minor = user_number < secret_number

    print("Your number is: ", user_number_str)

    if win:
        print("You win!")
    else:
        if major:
            print("You loose! Try a minor number.")
        elif minor:
            print("You loose! Try a major number.")

    tentative = tentative + 1

print("Game over")
