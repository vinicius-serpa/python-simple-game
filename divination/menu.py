import divination
import hangman

print("*********************************")
print("********Choose your game!********")
print("*********************************")

game = int(input("Choose your game: (1) Divination, (2) Hangman: "))

if (game == 1):
    divination.play()
elif (game == 2):
    hangman.play()