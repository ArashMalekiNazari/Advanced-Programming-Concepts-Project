from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class StatusCommand(Command):
    """
    The StatusCommand class represents a command that displays
    the current status of the player.

    This includes the player's location, remaining time,
    and the languages the player can communicate with.
    """

    # The action cost associated with executing this command
    COST: int = 0

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the status command.

        Prints information about the player's current state, including
        location, remaining time, and known languages.
        """
        loc = player.get_current_location()

        print("\n===== PLAYER STATUS =====")
        print("current Location: " + loc.get_name())
        print("Time Remaining: " + str(player.get_time_remaining()))

        # Languages player knows
        # just in case :)
        if len(player.get_languages()) == 0:
            print("Languages you can communicate with: (none)")
        else:
            line = "Languages you can communicate with: [ "
            for lang in player.get_languages():
                line += str(lang) + " "
            line += "]"
            print(line)

        print("==========================")
        game.handle_action_cost(StatusCommand.COST)
