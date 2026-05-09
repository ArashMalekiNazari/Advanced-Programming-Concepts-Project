"""
The Main module serves as the entry point of the application.

It initializes the game and starts the gameplay loop.
"""

from game import Game


def main():
    """
    The main function that launches the game.
    """
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
