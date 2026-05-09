from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class TakeCommand(Command):
    """
    The TakeCommand class represents a command that allows the player
    to pick up an item from the current location.

    When executed, this command attempts to move an item from the
    location's ground items into the player's inventory.
    """

    # The action cost associated with executing this command
    COST: int = 1

    def __init__(self, item_name: str):
        """
        Constructs a TakeCommand for a specific item.

        :param item_name: the name of the item to take
        """
        self._item_name = item_name

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the take command.

        Checks whether the specified item exists in the current
        location, attempts to add it to the player's inventory, and removes
        it from the location if successful.
        """
        location = player.get_current_location()

        # Find item safely using Location API
        target_item = location.get_item_by_name(self._item_name)

        if target_item is None:
            print("There is no item '" + self._item_name + "' in this location.")
            game.handle_action_cost(TakeCommand.COST)
            return

        # Try adding to inventory
        added = player.get_inventory().add_item(target_item)
        if not added:
            print("Your inventory is full. You cannot take '" + target_item.get_name() + "'.")
            game.handle_action_cost(TakeCommand.COST)
            return

        # Remove item SAFELY using Location API (not list returned by getter!)
        location.remove_item_by_name(self._item_name)

        print("You picked up the " + target_item.get_name() + ".")
        game.handle_action_cost(TakeCommand.COST)
