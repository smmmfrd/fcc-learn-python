# Rock Paper Scissors 2

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    playerinput = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

    playerchoice = int(playerinput)

    if playerchoice < 1 or playerchoice > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerinput = random.choice("123")

    computerchoice = int(computerinput)

    print("\nYou chose " + str(RPS(playerchoice)).replace("RPS.", "") + ".")
    print("Computer chose " + str(RPS(computerchoice)).replace("RPS.", "") + ".\n")

    if playerchoice == 1 and computerchoice == 3:
        print("🎉 You win!")
    elif playerchoice == 2 and computerchoice == 1:
        print("🎉 You win!")
    elif playerchoice == 3 and computerchoice == 2:
        print("🎉 You win!")
    elif playerchoice == computerchoice:
        print("😲 Tie game!")
    else:
        print("🐍 Python won!")

    restartchoice = input("\nPlay again?\nY for Yes\nQ to Quit\n\n")

    if restartchoice.lower() == "y":
        continue
    else:
        print("\n🎉 🎉 🎉 🎉 ")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye!")
