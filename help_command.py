from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class HelpCommand(Command):
    """
    The HelpCommand class represents a command that displays
    a list of valid commands and their descriptions.

    This command helps the player understand how to interact
    with the game by showing available actions.
    """

    # The action cost associated with executing this command
    COST: int = 0

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the help command.

        Prints all available commands along with brief explanations of
        what each command does.
        """
        print("\n========== HELP ==========")
        print("Available commands:\n")

        print("• go <direction>")
        print("      Move to another location (north / south).")
        print("• look")
        print("      See the description of your surroundings.")
        print("• status")
        print("      Show your current state (time, inventory, location).")
        print("• take <item>")
        print("      Pick up an item from the ground.")
        print("• drop <item>")
        print("      Drop an item to the ground.")
        print("• use <item>")
        print("      Use an item from your inventory.")
        print("• talk <character>")
        print("      Speak with someone in the location.")
        print("• inventory")
        print("      Shows all items you're carrying.")
        print("• quit")
        print("      Exit the game.")
        print("• help")
        print("      Show this help menu again.")

        print("===========================\n")

        game.handle_action_cost(HelpCommand.COST)
