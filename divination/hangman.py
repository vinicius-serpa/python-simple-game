import random


def play():
    print("*********************************")
    print("**********Hangman Game!**********")
    print("*********************************")

    # list [], tuple (), set {}, dictionary {key : value}

    with open("secret_words.txt", "r") as words_file:
        words_list = [line.strip().lower() for line in words_file]

    selected_index = random.randrange(0, len(words_list))
    secret_word = words_list[selected_index]

    correct_chars = ["_" for c in secret_word]  # list comprehensions
    total_errors = 6
    errors = 0
    hanged = False
    win = False

    print("Try a word with {} chars: {}".format(len(correct_chars), correct_chars))

    while (not(hanged) and not(win)):

        user_char = input("Type an character: ")
        user_char = user_char.strip().lower()

        index = 0

        if (user_char in secret_word):
            for c in secret_word:
                if (c == user_char):
                    correct_chars[index] = c
                index += 1
            for c in correct_chars:
                print(c, end=" ")
            print("")

        else:
            errors += 1
            print("You have {} tentatives".format(total_errors - errors))

        if (errors == total_errors):
            hanged = True

        if ("_" not in correct_chars):
            win = True

    if (win):
        print("You win!")
    elif (hanged):
        print("You loose!")

    print("Game over")


if (__name__ == "__main__"):
    play()
