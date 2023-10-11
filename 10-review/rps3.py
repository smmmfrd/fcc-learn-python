# Rock Paper Scissors 3 - Recursion

import sys
import random
from enum import Enum


def play_rps():
	class RPS(Enum):
		ROCK = 1
		PAPER = 2
		SCISSORS = 3

	playerinput = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

	playerchoice = int(playerinput)

	if(playerchoice not in [1,2,3]):
		print("You must enter 1, 2, or 3.")
		return play_rps()

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

	print("\nPlay again?")

	while True:
		restartchoice = input("\nY for Yes\nQ to Quit\n\n")
		if restartchoice.lower() not in ["y", "q"]:
			continue
		else:
			break

	if restartchoice.lower() == "y":
		return play_rps()
	else:
		print("\n🎉 🎉 🎉 🎉 ")
		print("Thank you for playing!\n")
		playagain = False


play_rps()

sys.exit("Bye!")
