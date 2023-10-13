# Rock Paper Scissors 7 - Modules

import random
from enum import Enum

def rps():
	game_count = 0
	player_wins = 0
	python_wins = 0

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
		
		print(f"\nYou chose{str(RPS(playerchoice)).replace('RPS.', '')}.")
		print(f"Computer chose {str(RPS(computerchoice)).replace('RPS.', '')}.\n")

		nonlocal player_wins, python_wins

		def winner_message():
			nonlocal player_wins, python_wins

			if playerchoice == 1 and computerchoice == 3:
				player_wins += 1
				return "🎉 You win!"
			elif playerchoice == 2 and computerchoice == 1:
				player_wins += 1
				return "🎉 You win!"
			elif playerchoice == 3 and computerchoice == 2:
				player_wins += 1
				return "🎉 You win!"
			elif playerchoice == computerchoice:
				return "😲 Tie game!"
			else:
				python_wins += 1
				return "🐍 Python won!"

		gameresult = winner_message()
		print(gameresult)

		nonlocal game_count
		game_count += 1

		print(f"\nGame count: {game_count}")
		print(f"\nPlayer Wins: {player_wins}")
		print(f"\nPython Wins: {python_wins}")

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
		
	return play_rps()


rock_paper_scissors = rps

if __name__ == "__main__":
	rock_paper_scissors()