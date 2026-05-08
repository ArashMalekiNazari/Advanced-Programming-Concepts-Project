from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class ExplainCommand(Command):
    """
    The ExplainCommand class represents a command that explains the
    game's storyline and objectives to the player.

    When executed, this command prints an overview of the game scenario,
    the player's goal, and the conditions required to win.
    """

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the explain command.

        Displays the game background, objectives, and success conditions
        to the player.
        """
        print("\n===== GAME EXPLANATION =====\n")

        print("You are on a train heading to a life-changing job interview.")
        print("Suddenly, the train stops due to an engine failure.")
        print("The mechanic is trying to fix the engine, but he needs help.")
        print()
        print("Your goal:")
        print("- Find useful tool(s).")
        print("- Move to the Engine Coach and help the mechanic fix the engine.")
        print("- Complete this before your time runs out!")
        print()
        print("Fix the engine before time expires… Good luck!")
        print("\n============================\n")
