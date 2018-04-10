import random


def play():

    print_header()
    secret_word = get_secret_word()
    correct_chars_list = initialize_correct_list(secret_word)
    total_errors = 7
    errors = 0
    hanged = False
    win = False

    print("Try a word with {} chars: {}".format(len(correct_chars_list), correct_chars_list))

    while (not(hanged) and not(win)):

        user_char = get_user_char()

        if (user_char in secret_word):
            index = 0
            for c in secret_word:
                if (c == user_char):
                    correct_chars_list[index] = c
                index += 1
            for c in correct_chars_list:
                print(c, end=" ")
            print("")

        else:
            errors += 1
            draw_hang(errors)
            print("You have {} tentatives".format(total_errors - errors))

        if (errors == total_errors):
            hanged = True

        if ("_" not in correct_chars_list):
            win = True

    print_final_message(win, hanged, secret_word)


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


def get_user_char():
    user_char = input("Type an character: ")
    return user_char.strip().lower()


def print_final_message(win, hanged, secret_word):
    if (win):
        print_winner_message()
    elif (hanged):
        print_looser_message(secret_word)


def print_looser_message(secret_word):
    print("Ohhhh, you was hanged!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_winner_message():
    print("Congratulations, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    play()