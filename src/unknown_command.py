from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class UnknownCommand(Command):
    """
    The UnknownCommand class represents an unrecognized or invalid command.

    This command is executed when the player's input does not match
    any valid command in the game.
    """

    # The action cost associated with executing this command
    COST: int = 1

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the unknown command.

        Informs the player that the command is not recognized
        and applies the corresponding action cost.
        """
        print("Unknown command!")
        game.handle_action_cost(UnknownCommand.COST)
