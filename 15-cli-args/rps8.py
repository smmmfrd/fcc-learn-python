# Rock Paper Scissors 8 -

import sys
import random
from enum import Enum


def rps(name="Player 1"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerinput = input(
            f"\n{name.title()}, please enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n"
        )

        playerchoice = int(playerinput)

        if playerchoice not in [1, 2, 3]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        computerinput = random.choice("123")

        computerchoice = int(computerinput)

        print(f"\n{name}, you chose {str(RPS(playerchoice)).replace('RPS.', '')}.")
        print(f"Computer chose {str(RPS(computerchoice)).replace('RPS.', '')}.\n")

        nonlocal player_wins, python_wins

        def winner_message():
            nonlocal player_wins, python_wins, name

            if playerchoice == 1 and computerchoice == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif playerchoice == 2 and computerchoice == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif playerchoice == 3 and computerchoice == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif playerchoice == computerchoice:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python won!\nSorry, {name}... 😢"

        gameresult = winner_message()
        print(gameresult)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s Wins: {player_wins}")
        print(f"\nPython Wins: {python_wins}")

        print(f"\nPlay again, {name}?")

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
            sys.exit(f"By {name}! 👋")

    return play_rps()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
