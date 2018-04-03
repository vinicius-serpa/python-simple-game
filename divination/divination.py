print("*********************************")
print("Divination Game!")
print("*********************************")

secret_number = 42

user_number_str = input("Type your number: ")
print("Your number is: ", user_number_str)
user_number = int(user_number_str)

if secret_number == user_number:
    print("You win!")
else:
    print("You loose!")

print("Game over")
