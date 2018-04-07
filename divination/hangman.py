def play():
    print("*********************************")
    print("**********Hangman Game!**********")
    print("*********************************")

    secret_word = "banana"
    total_tentatives = 6
    tentative = 1
    hanged = False
    win = False

    while (not(hanged) and not(win) and tentative <= total_tentatives):
        print("playing...")

        user_char = input("Type an character: ")

        index = 0

        for c in secret_word:
            if (c == user_char):
                print("Find char {} at position {}".format(c, index))
            index = index + 1

        tentative = tentative + 1

    print("Game over")


if (__name__ == "__main__"):
    play()
