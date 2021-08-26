import random

numbers = [1, 2, 3, 4, 5, 6]


class Dice:
    def roll_dice(self):
        while True:
            IA_Dice = random.choice(numbers)
            return IA_Dice


while True:
    Output = Dice.roll_dice(numbers)
    print(Output)
    play_again = input("Want to throw dice again? (Y)es/(N)o ").upper()
    if play_again != "Y":
        break
