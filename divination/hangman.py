import random


def play():

    print_header()
    secret_word = get_secret_word()
    correct_chars_list = initialize_correct_list(secret_word)
    total_errors = 6
    errors = 0
    hanged = False
    win = False

    print("Try a word with {} chars: {}".format(len(correct_chars_list), correct_chars_list))

    while (not(hanged) and not(win)):

        user_char = input("Type an character: ")
        user_char = user_char.strip().lower()

        index = 0

        if (user_char in secret_word):
            for c in secret_word:
                if (c == user_char):
                    correct_chars_list[index] = c
                index += 1
            for c in correct_chars_list:
                print(c, end=" ")
            print("")

        else:
            errors += 1
            print("You have {} tentatives".format(total_errors - errors))

        if (errors == total_errors):
            hanged = True

        if ("_" not in correct_chars_list):
            win = True

    if (win):
        print("You win!")
    elif (hanged):
        print("You loose!")

    print("Game over")


def print_header():
    print("*********************************")
    print("**********Hangman Game!**********")
    print("*********************************")


def get_secret_word():
    # list [], tuple (), set {}, dictionary {key : value}
    with open("secret_words.txt", "r") as words_file:
        words_list = [line.strip().lower() for line in words_file]
    selected_index = random.randrange(0, len(words_list))
    return words_list[selected_index]


def initialize_correct_list(word):
    return ["_" for c in word]  # list comprehensions


if (__name__ == "__main__"):
    play()