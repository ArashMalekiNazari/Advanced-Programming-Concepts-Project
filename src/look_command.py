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

    # The action cost associated with executing this command
    COST: int = 0

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the look command.

        Checks whether the player can see in the current location.
        If visibility conditions are met, prints detailed information
        about the location.
        """
        location = player.get_current_location()
        if not location.can_see():
            print("this coach is dark! Maybe you need a light to see what's here!")
            return

        # if the location itself is dark only if candle is inside this
        # location, the coach will be visible
        if location.is_dark():
            light = False
            for item in location.get_ground_items():
                if item.get_name().lower() == "candle":
                    light = True
                    break
            if not light:
                print("You need a light to see what's here!")
                return

        print("location:\n" + location.get_name())
        print("Description:\n" + location.get_description())
        print("Ground Items:\n" + location.show_ground_items())
        print("Characters:\n" + location.show_characters())
        print("Exits:\n" + location.show_exits())

        game.handle_action_cost(LookCommand.COST)
