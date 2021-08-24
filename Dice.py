import random

numbers = [1, 2, 3, 4, 5, 6]

while True:
    IA_Dice = random.choice(numbers)
    print(IA_Dice)

    play_again = input("Want to throw dice again? (Y)es/(N)o ").upper()
    if play_again != "Y":
        break