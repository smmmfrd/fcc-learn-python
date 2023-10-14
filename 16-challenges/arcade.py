import sys
from rps_challenge import rps
from guess_number import guessnumber


def arcade(playername):
    while True:
        print(f"\n{playername}, welcome to the arcade! 🤖")

        gamechoice = ""
        while True:
            gamechoice = input(
                '\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr enter "x" to exit the arcade.\n\n'
            )
            if gamechoice in "12x":
                break
            else:
                continue

        if gamechoice == "1":
            game = rps(playername)
            game()
        elif gamechoice == "2":
            game = guessnumber(playername)
            game()
        else:
            sys.exit(f"Bye {playername}")


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

    arcade(args.name)
