from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class LookCommand(Command):
    """
    The LookCommand class represents a command that allows the player
    to observe their current location.

    When executed, this command displays information about the current
    location, including its description, visible items, characters,
    and available exits, provided the player can see.
    """

    COST: int = 0

    def execute(self, player: Player, game: Game) -> None:
        """
        Executes the look command.

        Checks whether the player can see in the current location.
        If visibility conditions are met, prints detailed information
        about the location.
        """
        location = player.get_current_location()

        # can_see() returns True if the location is not dark,
        # or if a candle is currently present on the ground
        if not location.can_see():
            print("This coach is dark! Maybe you need a light to see what's here!")
            return

        print(f"Location:\n{location.get_name()}")
        print(f"Description:\n{location.get_description()}")
        print(f"Ground Items:\n{location.show_ground_items()}")
        print(f"Characters:\n{location.show_characters()}")
        print(f"Exits:\n{location.show_exits()}")

        game.handle_action_cost(LookCommand.COST)