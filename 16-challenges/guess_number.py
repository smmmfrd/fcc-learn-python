import random
import sys


def guessnumber(playername):
    gamesplayed = 0
    playerwins = 0

    def game():
        nonlocal playername, gamesplayed, playerwins

        playerinput = input(
            f"\n{playername}, try to guess which number I'm thinking of... 1, 2, or 3...\n\n"
        )

        while playerinput not in "123":
            playerinput = input(f"\n{playername}, please enter 1, 2, or 3.\n\n")

        compchoice = random.choice("123")

        print(
            f"\n{playername} the computer chose {compchoice}, you chose {playerinput}."
        )

        if compchoice == playerinput:
            playerwins += 1
            print("Great Job! You guessed right!")
        else:
            print(f"Sorry, {playername}, better luck next time.")

        gamesplayed += 1

        print(f"{'Game count:' :<30}{'' : >10}{gamesplayed}")
        print(f"{playername}'s{' wins:' : <30}{'' : >5}{playerwins}")
        print(
            f"{'Your winning percentage:':<30}{'' : >6}{(playerwins / gamesplayed):.2%}"
        )

        playagain = input(
            f"\n{playername}, would you like to play again? (Y for yes, Q to quit)\n"
        )

        if playagain.lower() == "y":
            return game()
        else:
            print("\n🎉 🎉 🎉 🎉 ")
            print("Thank you for playing!\n")

            if __name__ == "__main__":
                sys.exit(f"Bye {playername}! 👋")
            else:
                return

    return game


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

    play_guess_number = guessnumber(args.name)
    play_guess_number()
